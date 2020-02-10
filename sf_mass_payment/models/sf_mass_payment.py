from odoo import fields, models, api, _


class AccountMassPayment(models.Model):
    _name = 'sf.account.mass.payment'

    name = fields.Char(compute='_default_name_get')

    payment_id = fields.Many2one(
        comodel_name='account.payment',
        string='Payment',
        required=False)

    payment_date = fields.Date(
        string='Payment Date',
        default=lambda self: fields.Date.today(),
        required=False)

    company_id = fields.Many2one(
        comodel_name='res.company',
        string='Company',
        default=lambda self: self.env.user.company_id.id,
        required=False)

    state = fields.Selection(
        string='State',
        selection=[('draft', 'Draft'), ('post', 'Post'), ('done', 'Done')],
        default='draft',
        required=False, )

    payment_type = fields.Selection(
        [('outbound', 'Send Money'),
         ('inbound', 'Receive Money')],
        default='outbound',
        string='Payment Type', required=True)

    payment_method_id = fields.Many2one('account.payment.method', string='Payment Method Type', required=True,
                                        oldname="payment_method",
                                        domain=[('code', '=', 'check_printing')],
                                        help="Manual: Get paid by cash, check or any other method outside of Odoo.\n" \
                                             "Electronic: Get paid automatically through a payment acquirer by requesting a transaction on a card saved by the customer when buying or subscribing online (payment token).\n" \
                                             "Check: Pay bill by check and print it from Odoo.\n" \
                                             "Batch Deposit: Encase several customer checks at once by generating a batch deposit to submit to your bank. When encoding the bank statement in Odoo, you are suggested to reconcile the transaction with the batch deposit.To enable batch deposit, module account_batch_payment must be installed.\n" \
                                             "SEPA Credit Transfer: Pay bill from a SEPA Credit Transfer file you submit to your bank. To enable sepa credit transfer, module account_sepa must be installed ")

    payment_method_code = fields.Char(related='payment_method_id.code',
                                      help="Technical field used to adapt the interface to the payment type selected.",
                                      readonly=True)

    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Vendor',
        domain=[('supplier', '=', True)],
        required=True)

    journal_id = fields.Many2one(
        comodel_name='account.journal',
        string='Payment Journal',
        domain=[('type', '=', 'bank')],
        required=True)

    invoice_ids = fields.One2many(
        comodel_name='account.invoice',
        inverse_name='mass_payment_id',
        string='Bills',
        required=False)

    @api.depends('partner_id')
    def _default_name_get(self):
        for rec in self:
            rec.name = 'MP/{}'.format(rec.partner_id.name)

    @api.multi
    def action_confirm_payments(self):
        for record in self:
            record.payment_id.post()
        self.write({'state': 'done'})

    @api.multi
    def create_mass_payment(self):
        for record in self:
            currency = record.journal_id.currency_id or record.company_id.currency_id
            payment_methods = record.journal_id.outbound_payment_method_ids

            amount_total = sum(record.invoice_ids.mapped('amount_total'))
            invoice_ids = record.invoice_ids.mapped('id')

            payment = self.env['account.payment'].create({
                'payment_method_id': record.payment_method_id.id,
                'payment_type': 'outbound',
                'partner_id': record.partner_id.id,
                'partner_type': 'supplier',
                'journal_id': record.journal_id.id,
                'payment_date': record.payment_date,
                'invoice_ids': [(6, 0, invoice_ids)],
                'currency_id': currency.id,
                'amount': abs(amount_total),
                'check_amount_in_words': currency.amount_to_text(amount_total) if currency else False,
                'communication': self._get_communication(payment_methods[0] if payment_methods else False),
                # 'name': _("Bank Statement %s") % record.payment_date,
            })

            self.write({'state': 'post', 'payment_id': payment.id})

    def _get_communication(self, payment_method_id):
        return self.name or ''

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    mass_payment_id = fields.Many2one(
        comodel_name='sf.account.mass.payment',
        string='Payment',
        required=False)


# class AccountPayments(models.Model):
#     _inherit = 'account.payment'
#
#     mass_payment_id = fields.Many2one(
#         comodel_name='sf.account.mass.payment',
#         string='Payment',
#         required=False)


