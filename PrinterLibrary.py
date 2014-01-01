def call_printer_support(lottoNumber):
    """write data to file if existing will override it"""
    file = open('status.txt', 'w')
    file.write('You lotto number is ' + lottoNumber + '\n')
    file.close()