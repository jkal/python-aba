"""
aba.records
~~~~~~~~~~~
An ABA (or Direct Entry) file contains 3 types of records:
- The Descriptive Record or Record Type 0 is the header line.
- The Detail Record or Record Type 1 is the line of each transaction.
- The File Total Record or Record Type 7 is the last line.
"""
from __future__ import absolute_import

from aba import exceptions
from aba import fields


class Record(object):
    """Validate and render a record (line)."""
    length = 120

    def render_to_string(self):
        output = ''
        for field in self.fields:
            output += str(field.render_to_string())

        # Check length
        if len(output) != self.length:
            raise exceptions.ValidationError(
                'length mismatch in {}'.format(self.__class__.__name__)
            )

        return output


class DescriptiveRecord(Record):

    def __init__(self, user_bank, user_name, user_number, description, date):
        self.fields = [
            fields.RecordType(0),
            fields.Blank(17),
            fields.ReelSequenceNumber(1),
            fields.UserBank(user_bank),
            fields.Blank(7),
            fields.UserName(user_name),
            fields.UserNumber(user_number),
            fields.Description(description),
            fields.Date(date),
            fields.Blank(40)
        ]


class DetailRecord(Record):

    def __init__(self, bsb, account_number, txn_code, amount, payee_name, lodgment_ref,
                 sender_bsb, sender_account, remitter_name, tax_amount=0):
        self.fields = [
            fields.RecordType(1),
            fields.BSB(bsb),
            fields.AccountNumber(account_number),
            fields.Blank(1),
            fields.TxnCode(txn_code),
            fields.Amount(amount),
            fields.PayeeName(payee_name),
            fields.LodgmentRef(lodgment_ref),
            fields.BSB(sender_bsb),
            fields.AccountNumber(sender_account),
            fields.RemitterName(remitter_name),
            fields.TaxAmount(tax_amount)
        ]

class TotalRecord(Record):

   def __init__(self, total_credit, total_debit, count):
       total_net = abs(total_credit - total_debit)

       self.fields = [
           fields.RecordType(7),
           fields.BSB('999-999'),
           fields.Blank(12),
           fields.Total(total_net),
           fields.Total(total_credit),
           fields.Total(total_debit),
           fields.Blank(24),
           fields.TotalCount(count),
           fields.Blank(40)
       ]
