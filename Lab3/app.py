from __future__ import print_function
from mailmerge import MailMerge
import os, comtypes.client, cdr, netflow as nf
from datetime import date

tel_num = input('Enter telephone number: ')
ip_addr = input('Enter IP address: ')

template = "invoice_templete.docx"

document = MailMerge(template)

# Insert information about bank
document.merge(
    bank_name = 'HT Bank',
    bik_num = '368521569',
    bank_acc_num = '6085214000525698050'
)

# Insert information about provider
document.merge(
    inn_num = '2568412560',
    kpp_num = '256820145',
    provider_name = 'OOO "HOLA"',
    provider_acc_num = '5214100698206328500'
)
# Insert information about client
document.merge(
    payment_number = str(99),
    payment_date = date.today().strftime("%d-%m-%Y"),
    provider_info = 'ООО "HOLA", ИНН 2568412560, КПП 256820145, 197022, СанктПетербург, Каменноостровский проспект, дом 44B, тел.: 89258962666',
    client_info = 'ООО "HKT", ИНН 8412566025, КПП 826401255, 197022, СанктПетербург, Большой проспект, дом 65, тел.: 89632025447'
)

# Insert information about services
scb = cdr.Subscriber(tel_num)
cdr_bill = scb.smsBill() + scb.originCallBill() + scb.destCallBill()
tf = nf.Traffic(ip_addr)
netflow = round(tf.getFlow()/1000, 2)
netflow_bill = round(tf.billing(), 2)
servicesList = [
    {
        'index' : '1',
        'service_name' : 'Услуг "Телефония"',
        'total' : str(cdr_bill)
    },
    {
        'index': '2',
        'service_name' : 'Услуг "Netflow"',
        'amount' : str(netflow),
        'unit' : 'МБ',
        'total': str(netflow_bill)
    }
]
document.merge_rows('index', servicesList)

# Insert information about bill
TAX = 20
payment_total_without_tax = cdr_bill + netflow_bill
payment_total = round(payment_total_without_tax * TAX / 100, 2)
document.merge(
    total_before_tax = str(payment_total_without_tax),
    tax = str(TAX) + '%',
    payment_total = str(payment_total),
    service_count = str(len(servicesList))
)
# Save file .docx
document.write('invoice.docx')

# Convert to pdf
wdFormatPDF = 17
cur_path = os.getcwd()
in_file = cur_path + "\invoice.docx"
out_file = cur_path + "\invoice.pdf"

word = comtypes.client.CreateObject('Word.Application')
doc = word.Documents.Open(in_file)
doc.SaveAs(out_file, FileFormat=wdFormatPDF)
doc.Close()
word.Quit()

os.remove('invoice.docx')

print('Complete invoice!')