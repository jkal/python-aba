"""
aba.generator
~~~~~~~~~~~~~
"""
from __future__ import absolute_import

from aba.records import *


class AbaFile(object):
    """Stores ABA records and generates a complete file."""

    def __init__(self, header):
        self.header = header
        self.records = []
        self.total_debit = 0
        self.total_credit = 0

    def add_record(self, record):
        self.records.append(record)

    def render_to_string(self, line_ending='\r\n'):
        output = self.header.render_to_string() + line_ending

        for record in self.records:
            if record.fields[4].value == '53':
                self.total_credit += int(record.fields[5].value)
            output += record.render_to_string() + line_ending

        total = TotalRecord(
            total_credit=self.total_credit,
            total_debit=self.total_debit,
            count=len(self.records)
        )
        output += total.render_to_string()

        return output