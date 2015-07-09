python-aba
==========

This is a tiny Python library for generating ABA/Cemtext/Direct Entry files
used by Australian banks for bulk payments.

Usage
-----
See example below.

.. code:: python

    import datetime
    from aba.generator import AbaFile
    from aba import records

    header = records.DescriptiveRecord(
        user_bank='NAB',
        user_name='AJAX CRACKERS',
        user_number=12345,
        description='SALARIES',
        date=datetime.date(day=05, month=02, year=2000)
    )

    entry = records.DetailRecord(
        bsb='123-456',
        account_number='123456',
        txn_code=53,
        amount=4242,
        payee_name='HACKER, J. RANDOM',
        lodgment_ref='RANDOM PAYMENT',
        sender_bsb='987-654',
        sender_account='445566777',
        remitter_name='AJAX CRACKERS',
    )

    aba_file = AbaFile(header)
    aba_file.add_record(entry)
    print aba_file.render_to_string()


