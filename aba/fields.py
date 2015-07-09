"""
aba.fields
~~~~~~~~~~
"""
from __future__ import absolute_import

from aba import exceptions


class Field(object):
    """Generic field with helper methods."""
    length = None
    valid_values = ()
    value = None

    def validate(self):
        if len(self.value) != self.length:
            raise exceptions.ValidationError(
                'length mismatch in {}'.format(self.__class__.__name__)
            )

        if self.valid_values:
            if self.value not in self.valid_values:
                raise exceptions.ValidationError(
                    'invalid value in {}'.format(self.__class__.__name__)
                )

    def render_to_string(self):
        self.value = str(self.value)
        self.validate()
        return self.value


class RecordType(Field):
    """
    Must be '0' in Descriptive record, '1' in Detail record and '7' in Total
    record.
    """
    length = 1
    valid_values = ('0', '1', '7')

    def __init__(self, type_id):
        self.value = type_id


class Blank(Field):
    """Represents a string field with spaces."""
    fillchar = ' '

    def __init__(self, length):
        self.length = length
        self.value = self.fillchar * self.length


class ReelSequenceNumber(Field):
    """Must be numeric commencing at 01."""
    length = 2

    def __init__(self, value):
        self.value = str(value).rjust(self.length, '0')


class UserBank(Field):
    """
    Must be approved Financial Institution abbreviation.

    For example, Bank of Queensland's abbreviation is BQL, Westpac's abbreviation
    is "WBC". Consult your Bank for correct abbreviation.
    """
    length = 3

    def __init__(self, name):
        self.value = name


class UserName(Field):
    """
    Must be User Preferred Specification as advised by User's FI.
    Left justified, blank filled. All coded character set valid.
    Must not be all blanks.
    """
    length = 26

    def __init__(self, name):
        self.value = str(name).ljust(self.length, ' ')


class UserNumber(Field):
    """
    Must be User Identification Number which is allocated by APCA.
    Must be numeric, right justified, zero filled.
    """
    length = 6

    def __init__(self, number):
        self.value = str(number).rjust(self.length, '0')


class Description(Field):
    length = 12

    def __init__(self, description):
        self.value = str(description).ljust(self.length, ' ')


class Date(Field):
    """
    Must be numeric in the formal of DDMMYY. Must be a valid date. Zero filled.
    """
    length = 6

    def __init__(self, date):
        self.value = date.strftime('%d%m%y')


class BSB(Field):
    length = 7

    def __init__(self, bsb):
        self.value = bsb


class AccountNumber(Field):
    length = 9

    def __init__(self, number):
        self.value = number.rjust(self.length, ' ')


class TxnCode(Field):
    length = 2
    valid_values = ('50', '53')

    def __init__(self, number):
        self.value = number


class Amount(Field):
    length = 10

    def __init__(self, amount):
        self.value = str(amount).rjust(self.length, '0')


class PayeeName(Field):
    length = 32

    def __init__(self, name):
        self.value = name.ljust(self.length, ' ')


class LodgmentRef(Field):
    length = 18

    def __init__(self, ref):
        self.value = ref.ljust(self.length, ' ')


class RemitterName(UserName):
    length = 16


class TaxAmount(Field):
    length = 8

    def __init__(self, amount):
        self.value = str(amount).rjust(self.length, '0')


class Total(Field):
    length = 10

    def __init__(self, amount):
        self.value = str(amount).rjust(self.length, '0')


class TotalCount(Total):
    length = 6

