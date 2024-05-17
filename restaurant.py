from tkinter import *
import time
import calc_function
import random

root=Tk()

root.geometry("1200x700")

root.title("Restaurant Payment System")

top=Frame(root,width=1200, height=50)
top.pack(side=TOP)
frame1=Frame(root,width=700,height=550)
frame1.pack(side=LEFT)
frame2=Frame(root,width=400,height=550)
frame2.pack(side=RIGHT)

app_title=Label(top,font=('arial',30,'bold'),text='Restaurant Payment System')
app_title.grid(row=0,column=0)

localtime=time.asctime(time.localtime(time.time()))
app_time=Label(top,font=('arial',20),text=localtime)
app_time.grid(row=1,column=0)


calc_function.calculator(frame2)


fries=StringVar()
largefries=StringVar()
burger=StringVar()
filet=StringVar()
cheese_burger=StringVar()
drinks=StringVar()
order_no=StringVar()
cost=StringVar()
service_charge=StringVar()
tax=StringVar()
subtotal=StringVar()
total=StringVar()


price_list={'fries': 2.5, 'largefries':3.5,'burger':5.5,'filet':4.5,'cburger':6.0,'drinks':2.5}


def bill():
    x=str(random.randint(10000,99999))
    order_no.set(x)

    count_of_fries=int(fries.get())
    count_of_largefries=int(largefries.get())
    count_of_burger=int(burger.get())
    count_of_filet=int(filet.get())
    count_of_cheese=int(cheese_burger.get())
    count_of_drinks=int(drinks.get())

    cost_of_fries=count_of_fries * price_list['fries']
    cost_of_largefries=count_of_largefries * price_list['largefries']
    cost_of_burger=count_of_burger * price_list['burger']
    cost_of_filet=count_of_filet * price_list['filet']
    cost_of_cheese=count_of_cheese * price_list['cburger']
    cost_of_drinks=count_of_drinks * price_list['drinks']

    cost_of_everything=cost_of_burger+cost_of_filet+cost_of_cheese+cost_of_largefries+cost_of_fries+cost_of_drinks

    cost_of_meal="$" + str('%.2f'%(cost_of_everything))
    pay_tax=cost_of_everything * 0.1

    total_cost= cost_of_everything + pay_tax
    ser_charge=total_cost *0.125
    service='$'+ str('%.2f' % ser_charge)
    overall_cost= '$' + str('%.2f'% (total_cost +ser_charge))
    paid_tax='$' + str('%.2f'%pay_tax)

    service_charge.set(service)
    cost.set(cost_of_meal)
    tax.set(paid_tax)
    subtotal.set(cost_of_meal)
    total.set(overall_cost)

def exit():
    root.destroy()
def reset():
    fries.set("")
    largefries.set("")
    burger.set("")
    filet.set("")
    cheese_burger.set("")
    drinks.set("")
    order_no.set("")
    cost.set("")
    service_charge.set("")
    tax.set("")
    subtotal.set("")
    total.set("")

def price():
    r=Tk()
    r.geometry("600x300")
    r.title("Price List")

    lblinfo=Label(r,font=('arial',20,'bold'),text='ITEM',fg='black')
    lblinfo.grid(row=0,column=0)

    lblinfo=Label(r,font=('arial',20,'bold'),text='PRICE',fg='black')
    lblinfo.grid(row=0,column=1)

    lblinfo=Label(r,font=('arial',15,'bold'),text='Fries',fg='black')
    lblinfo.grid(row=1,column=0)
    lblinfo=Label(r,font=('arial',15,'bold'),text="$"+str('%.2f'%price_list['fries']),fg='black')
    lblinfo.grid(row=1,column=1)

    lblinfo=Label(r,font=('arial',15,'bold'),text='Large Fries',fg='black')
    lblinfo.grid(row=2,column=0)
    lblinfo=Label(r,font=('arial',15,'bold'),text="$"+str('%.2f'%price_list['largefries']),fg='black')
    lblinfo.grid(row=2,column=1)

    lblinfo=Label(r,font=('arial',15,'bold'),text='Burger',fg='black')
    lblinfo.grid(row=3,column=0)
    lblinfo=Label(r,font=('arial',15,'bold'),text="$"+str('%.2f'%price_list['burger']),fg='black')
    lblinfo.grid(row=3,column=1)

    lblinfo=Label(r,font=('arial',15,'bold'),text='Filet',fg='black')
    lblinfo.grid(row=4,column=0)
    lblinfo=Label(r,font=('arial',15,'bold'),text="$"+str('%.2f'%price_list['filet']),fg='black')
    lblinfo.grid(row=4,column=1)

    lblinfo=Label(r,font=('arial',15,'bold'),text='Cheese Burger',fg='black')
    lblinfo.grid(row=5,column=0)
    lblinfo=Label(r,font=('arial',15,'bold'),text="$"+str('%.2f'%price_list['cburger']),fg='black')
    lblinfo.grid(row=5,column=1)

    lblinfo=Label(r,font=('arial',15,'bold'),text='Drink',fg='black')
    lblinfo.grid(row=6,column=0)
    lblinfo=Label(r,font=('arial',15,'bold'),text="$"+str('%.2f'%price_list['drinks']),fg='black')
    lblinfo.grid(row=6,column=1)

    r.mainloop()

lblfries=Label(frame1,font=('arial',16,'bold'),text='Fries')
lblfries.grid(row=0,column=0)
textfries=Entry(frame1,font=('arial',16,'bold'),textvariable=fries,bd=6,bg='white',justify='right')
textfries.grid(row=0,column=1)


lbllargefries=Label(frame1,font=('arial',16,'bold'),text='Largefries')
lbllargefries.grid(row=1,column=0)
textlargefries=Entry(frame1,font=('arial',16,'bold'),textvariable=largefries,bd=6,bg='white',justify='right')
textlargefries.grid(row=1,column=1)


lblburger=Label(frame1,font=('arial',16,'bold'),text='Burger')
lblburger.grid(row=2,column=0)
textburger=Entry(frame1,font=('arial',16,'bold'),textvariable=burger,bd=6,bg='white',justify='right')
textburger.grid(row=2,column=1)

lblfilet=Label(frame1,font=('arial',16,'bold'),text='Filet')
lblfilet.grid(row=3,column=0)
textfilet=Entry(frame1,font=('arial',16,'bold'),textvariable=filet,bd=6,bg='white',justify='right')
textfilet.grid(row=3,column=1)

lblcheese=Label(frame1,font=('arial',16,'bold'),text='Cheese Burger')
lblcheese.grid(row=4,column=0)
textcheese=Entry(frame1,font=('arial',16,'bold'),textvariable=cheese_burger,bd=6,bg='white',justify='right')
textcheese.grid(row=4,column=1)

lbldrinks=Label(frame1,font=('arial',16,'bold'),text='Drinks')
lbldrinks.grid(row=5,column=0)
textdrinks=Entry(frame1,font=('arial',16,'bold'),textvariable=drinks,bd=6,bg='white',justify='right')
textdrinks.grid(row=5,column=1)


# Preparing the output display

lblorderno=Label(frame1,font=('arial',16,'bold'),text='Order No',fg='steel blue',)
lblorderno.grid(row=0, column=2)
txtorderno=Entry(frame1, font =('arial',16,'bold'),textvariable=order_no,bd=6,bg="powder blue",justify="right")
txtorderno.grid(row=0,column=3)
 

lblcost=Label(frame1,font=('arial',16,'bold'),text='Cost',fg='steel blue',)
lblcost.grid(row=1, column=2)
textcost=Entry(frame1, font =('arial',16,'bold'),textvariable=cost,bd=6,bg="powder blue",justify="right")
textcost.grid(row=1,column=3)

lblservicecharge=Label(frame1,font=('arial',16,'bold'),text='Service Charge',fg='steel blue',)
lblservicecharge.grid(row=2, column=2)
textservicecharge=Entry(frame1, font =('arial',16,'bold'),textvariable=service_charge,bd=6,bg="powder blue",justify="right")
textservicecharge.grid(row=2,column=3)

lbltax=Label(frame1,font=('arial',16,'bold'),text='Tax',fg='steel blue',)
lbltax.grid(row=3, column=2)
texttax=Entry(frame1, font =('arial',16,'bold'),textvariable=tax,bd=6,bg="powder blue",justify="right")
texttax.grid(row=3,column=3)

lblsubtotal=Label(frame1,font=('arial',16,'bold'),text='Sub Total',fg='steel blue',)
lblsubtotal.grid(row=4, column=2)
textsubtotal=Entry(frame1, font =('arial',16,'bold'),textvariable=subtotal,bd=6,bg="powder blue",justify="right")
textsubtotal.grid(row=4,column=3)

lbltotal=Label(frame1,font=('arial',16,'bold'),text='Total',fg='steel blue',)
lbltotal.grid(row=5, column=2)
texttotal=Entry(frame1, font =('arial',16,'bold'),textvariable=total,bd=6,bg="powder blue",justify="right")
texttotal.grid(row=5,column=3)


lbltotal1=Label(frame1,text="-",fg='white')
lbltotal1.grid(row=6,columnspan=4)

btnprice=Button(frame1,padx=16,pady=8,bd=10,fg='black',font=('arial',16,'bold'),width=10,text="PRICE",bg="powder blue",command=price)
btnprice.grid(row=7,column=0)

btntotal=Button(frame1,padx=16,pady=8,bd=10,fg='black',font=('arial',16,'bold'),width=10,text="TOTAL",bg="powder blue",command=bill)
btntotal.grid(row=7,column=1)

btnreset=Button(frame1,padx=16,pady=8,bd=10,fg='black',font=('arial',16,'bold'),width=10,text="RESET",bg="powder blue",command=reset)
btnreset.grid(row=7,column=2)

btnexit=Button(frame1,padx=16,pady=8,bd=10,fg='black',font=('arial',16,'bold'),width=10,text="EXIT",bg="powder blue",command=exit)
btnexit.grid(row=7,column=3)

root.mainloop() 