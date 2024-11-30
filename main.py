
from tkinter import *
window =Tk()



window.configure(bg="lightblue")
window.geometry('800x400')


window.title("Boycott Product Detector")
companies = (

    "Visa", "Caterpillar", "Hyundai Heavy Industries", "Alstom", "GE (General Electric)",
    "Bosch", "Sanofi", "GlaxoSmithKline (GSK)", "Novartis", "Abbott", "Eli Lilly",
    "Comcast", "Fox News", "Sony", "Warner Music Group", "Universal Music Group",
    "Ryanair", "Hilton Hotels", "Marriott", "Avis", "Hardees",
    "Apple", "Microsoft", "Google", "Amazon", "Facebook", "Mcdonald's", "KFC", ""
    "Tesla", "Samsung", "Intel", "IBM", "Cisco",
    "Oracle", "Adobe", "Salesforce", "Netflix", "PayPal",
    "Unilever", "Procter & Gamble", "Johnson & Johnson", "Pfizer", "Merck",
    "PepsiCo", "Coca-Cola", "Nestle", "Danone", "Kellogg's",
    "Boeing", "Lockheed Martin", "Airbus", "Siemens", "Hitachi",
    "Panasonic", "Sharp", "LG Electronics", "Xiaomi", "Huawei",
    "Tencent", "Alibaba", "eBay", "Walmart", "Target",
    "Costco", "FedEx", "UPS", "DHL", "Volkswagen",
    "Toyota", "Ford", "BMW", "Mercedes-Benz", "Nissan",
    "Audi", "Ferrari", "Lamborghini", "Porsche", "Rolls-Royce",
    "Hyatt", "InterContinental Hotels", "Delta Airlines", "American Airlines",
    "Southwest Airlines", "Qantas", "Etihad Airways", "Emirates"
)

def action ():
    keyword = input.get()
    if keyword in companies:
        label_3['text']='BOYCOTT'
        label_3["fg"]='red'
    else:
        label_3['text']='NOT BOYCOTT'
        label_3['fg']='green'


label_1 = Label(window,text='Boycott  Product  Detector', fg='black',bg='lightblue',font=('Times New Roman', 20, 'bold') )
label_1.place(relx=0.5, y=60, anchor="center") 

label_2 = Label(window,text='Enter The Brand Name : ',fg='black', font='bold')
label_2.place(x=50,y=150)

input = Entry(window,text='enter brand',width=30, fg ='black' , font='bold' )
input.place(x=250 , y=150)



btn = Button(window,text='Generate !',fg='white',bg='blue',font='bold',command=action)
btn.place(x=550,y=145)



label_3 = Label(window,text='....',font=('Times New Roman', 20, 'bold'),fg='red',bg='lightblue')
label_3.place(relx=0.5,y=250 , anchor="center")


window.mainloop()
