import PyPDF2

file_path = open("The_Living_World.pdf","rb")
pdfReader = PyPDF2.PdfFileReader(file_path)

all_pages = []
for i in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(i)
    all_pages.append(pageObj.extractText())

garbage_stuff = ['Aakash Educational Services Pvt. Ltd. \n- Regd. Office : Aakash Tower, 8, \nPusa Road, \nNew Delhi-1\n10005 Ph.011-47623456',
'Objective Type Questions', 'Chapter 1', 'The Living World', 'Solutions', 'SECTION - A','Solutions','of Assignment (Set-2)',
'SECTION - B','SECTION - C','SECTION - D','Previous Years Questions', ' [NEET (Phase-2)-2016]','[NEET-2016]','[NEET-2013]',
'[AIPMT (Prelims)-2012]','[AIPMT (Mains)-2011]','[AIPMT (Prelims)-2007]','Assertion - Reason Type Questions',
'4444\n4444\n44','4545\n4545\n45','4646\n4646\n46','4747\n4747\n47','4848\n4848\n48','4949\n4949\n49','5050\n5050\n50',
'5151\n5151\n51','5252\n5252\n52','5353\n5353\n53','5454\n5454\n54','5555\n5555\n55','5656\n5656\n56','5757\n5757\n57',
'5858\n5858\n58','5959\n5959\n59','6060\n6060\n60']


for i in range(pdfReader.numPages):
    for x in range(len(garbage_stuff)):
        all_pages[i] = all_pages[i].replace(garbage_stuff[x],' ')

for i in range(pdfReader.numPages):
    print(all_pages[i])
    print()
    print("---------------------------------------------------------------------------------------------------------------")
    print()
