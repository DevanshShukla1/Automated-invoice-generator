from docxtpl import DocxTemplate

doc = DocxTemplate("template.docx")

invoice_list = [[2, "Apple II", 0.5, 1],
                [1, "Macbook pro", 5, 5],
                [2, "Ipod", 2, 4]]


doc.render({"name":"Devansh", 
            "phone":"9766990012",
            "invoice_list": invoice_list,
            "subtotal":10,
            "salestax":"10%",
            "total":9})
doc.save("new_invoice.docx")

