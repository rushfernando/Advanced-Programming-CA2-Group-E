# -*- coding: utf-8 -*-


#Import the libraires and github modules in the programm
from tkinter import *#For making GUI
import tkinter.messagebox
import sqlite3#For making the database using SQL3

##############################################################################
#Make a class for the user interface module
class product_ui:
    
    #Step 1: Create a basic root path and the background of the UI
    def __init__(self,root):
        
        #Create an objecte refrace of database class
        dat = op_database()
        dat.connection()
        
        self.root = root
        self.root.title(' Warehouse inventory recorded database ')#Name of product
        self.root.geometry("900x690")#Dimention of the UI
        self.root.config(bg='silver')#Background color of UI
        
        ##Create a variable to store the product information befor adding labels
        product_id = StringVar()
        product_name = StringVar()
        product_Qty = StringVar()
        product_price = StringVar()
        product_company = StringVar()
        product_contect = StringVar()
        
        #Sub steps after setp 4 and class by
        '''Call the database methods to perfomed the DB operation'''
        
        #For closeing the GUI frame
        def close():
            print('Product: close process called')
            close = tkinter.messagebox.askyesno('Wearhouse invenry recorded',
                                                'Do you want to close the system')
            if close > 0:
                root.destroy()
                print('Product: Closed the entry system\n')
                
                
        #Make a funciton of clear button the to empty dataset
        def clear():
            print('Product:Clear the enetry in system\n')
            self.txtp_id.delete(0,END)
            self.txtp_name.delete(0,END)
            self.txtp_price.delete(0,END)
            self.txtp_qty.delete(0,END)
            self.txtp_compy.delete(0,END)
            self.txtp_cont.delete(0,END)
            print('Product: Clear processes is completed\n')
        
        #Create a function of insert button
        def sav_data():
            print('product: insert the enetry in system')
            if (len(product_id.get())!=0):
                dat.insert(product_id.get(), product_name.get(),
                           product_price.get(),product_Qty.get(),
                           product_company.get(), product_contect.get())
                
                iteamList.delete(0,END)
                iteamList.insert(END,product_id.get(), product_name.get(),
                                 product_price.get(),product_Qty.get(),
                                 product_company.get(), product_contect.get())
                
                ShowProductList()#Call the product list funciton After inserting data
            
            else:
                tkinter.messagebox.askyesno('Wearhouse invenry recorded',
                                                'Load product id')
                
            print('Product: Storing data entry is completed\n')
            
        #Create a function to display aviable products in scorel bar
        def ShowProductList():
            print('Product: ShowProductList is called')
            iteamList.delete(0,END)
            #Display the numer of iteams in the inventory
            for row in dat.display():
                iteamList.insert(END, row,str(''))
                print('Product: ShowProductList is completed\n')
                
                
        #Create a funciton to scrollbar to display the exact datapoint
        def product_reco(event):
            print('Product:product_reco process is called')
            global pd
            
            searchPd = iteamList.curselection()[0]
            pd = iteamList.get(searchPd)
            
            self.txtp_id.delete(0,END)
            self.txtp_id.insert(END, pd[0])
            
            self.txtp_name.delete(0,END)
            self.txtp_name.insert(END, pd[1])
            
            self.txtp_price.delete(0,END)
            self.txtp_price.insert(END, pd[2])
            
            self.txtp_qty.delete(0,END)
            self.txtp_qty.insert(END, pd[3])
            
            self.txtp_compy.delete(0,END)
            self.txtp_compy.insert(END, pd[4])
            
            self.txtp_cont.delete(0,END)
            self.txtp_cont.insert(END, pd[5])
        
            print('Product: product_reco process is completed\n')
            
        #Create a funciton to delete the products data points from DB
        def del_recod():
            print('Product:  delete procees is called')
            if (len(product_id.get())!=0):
                dat.delt(pd[0])
                clear()
                ShowProductList()
            print('Product:  delete procees is completed')
            
        #search data points in the database
        def search_db():
            print('Product: search the datapoints is called')
            iteamList.delete(0,END)
            for row in dat.search_butt(product_id.get(), 
                                       product_name.get(),
                                       product_price.get(),
                                       product_Qty.get(),
                                       product_company.get(), 
                                       product_contect.get()):
                iteamList.insert(END, row, str(''))
                
            print('Product: search the datapoints is completed')
        
                

        
########################################################################
        #Step 2 Add the title frame in the UI
        """Create a basic frame of th use to load the label"""
        MainFrame =Frame(self.root,bg='silver')
        MainFrame.grid()
        
        #Step2.1 Create a frame with header
        HeadFrame = Frame(MainFrame, bd=1, padx=50,
                         pady=10, bg='silver', relief=RIDGE)
        HeadFrame.pack(side=TOP)
        
        #Step2.2 Add the title of the UI
        self.Title = Label(HeadFrame, font=('Times New Roman', 30,'bold'),fg='darkgreen',
                          text=' Warehouse inventory recorder database ',
                          bg='silver')
        self.Title.grid()
       
        #Step 2.3 Add the Operation body frame into the UI
        '''Setup the UI body of operation frame 
        dimentions borders and padding buffers'''
        OperatingFrame = Frame(MainFrame, bd=2, width=1100, height = 50,
                              padx=50, pady=20, bg ='dimgray', relief=RIDGE)
        OperatingFrame.pack(side=BOTTOM)
        
#############################################################################
        #Step 3 Add the basic body frame
        UiBodyFrame = Frame(MainFrame, bd=2, width=1290, height = 400,
                              padx=30, pady=20, bg ='dimgray', relief=RIDGE)
        UiBodyFrame.pack(side=BOTTOM)
        
        #Step 3.2 Add the numbers of label frames into programme
        
        #Add the left pannel
        LeftSideFrame=LabelFrame(UiBodyFrame, bd=2, width=600, 
                                height = 400, padx=20, pady=10, bg='ivory', fg='navy',
                                relief=RIDGE, font=('Times New Roman',14, 'bold'),
                                text = '  |-*-*-*-*-* Product information -*-*-*-*-*-| ')
        LeftSideFrame.pack(side= LEFT)
        
        #Set the dummy to put a sapce between two frame
        dummyFrame=LabelFrame(UiBodyFrame, width = 10)
        dummyFrame.pack(side= LEFT)
        
        #Add the right pannel
        RightSideFrame=LabelFrame(UiBodyFrame, bd=2, width=500, 
                                height = 400, padx=20, pady=10, bg='ivory',fg='navy',
                                relief=RIDGE, font=('Times New Roman',14, 'bold'),
                                text = ' |-*-*-*-*-* Availability of Product -*-*-*-*-*-| ')
        RightSideFrame.pack(side=RIGHT)
        
        #Step 3.3 Add the widgest to the body fram
        ##Add the widgets of the left body frame
        
        #Add a product id variables label
        self.labelp_id= Label(LeftSideFrame, 
                                   font=('Times New Roman',12, 'bold'),
                                  text = 'Product ID:', padx = 2,pady=2,
                                  bg = 'ivory', fg = 'firebrick')
        self.labelp_id.grid(row = 2, column = 0, stick =W)
        
        self.txtp_id = Entry(LeftSideFrame, 
                                   font=('Times New Roman',13),
                                  textvariable = product_id, width= 30,)
        self.txtp_id.grid(row=2, column = 1, sticky = W)
        
         #Add a product name variables label
        self.labelp_name= Label(LeftSideFrame, 
                                   font=('Times New Roman',12, 'bold'),
                                  text = 'Product Name:', padx = 2,pady=2,
                                  bg = 'ivory', fg = 'firebrick')
        self.labelp_name.grid(row = 4, column = 0, stick =W)
        
        self.txtp_name = Entry(LeftSideFrame, 
                                   font=('Times New Roman',13),
                                  textvariable = product_name, width= 30,)
        self.txtp_name.grid(row=4, column = 1, sticky = W)
        
        #Add a product price variables label
        self.labelp_price= Label(LeftSideFrame, 
                                   font=('Times New Roman',12, 'bold'),
                                  text = 'Product Price:', padx = 2,pady=2,
                                  bg = 'ivory', fg = 'firebrick')
        self.labelp_price.grid(row = 6, column = 0, stick =W)
        
        self.txtp_price = Entry(LeftSideFrame, 
                                   font=('Times New Roman',13),
                                  textvariable = product_price, width= 30,)
        self.txtp_price.grid(row=6, column = 1, sticky = W)
        
        #Add a product quntites variables label
        self.labelp_qty= Label(LeftSideFrame, 
                                   font=('Times New Roman',12, 'bold'),
                                  text = 'Product quantity :', padx = 2,pady=2,
                                  bg = 'ivory', fg = 'firebrick')
        self.labelp_qty.grid(row = 8, column = 0, stick =W)
        
        self.txtp_qty = Entry(LeftSideFrame, 
                                   font=('Times New Roman',13),
                                  textvariable = product_Qty, width= 30,)
        self.txtp_qty.grid(row=8, column = 1, sticky = W)
        
        #Add a product compeny variables label
        self.labelp_compy= Label(LeftSideFrame, 
                                   font=('Times New Roman',12, 'bold'),
                                  text = 'Mfg. company:', padx = 2,pady=2,
                                  bg = 'ivory', fg = 'firebrick')
        self.labelp_compy.grid(row = 10, column = 0, stick =W)
        
        self.txtp_compy = Entry(LeftSideFrame, 
                                   font=('Times New Roman',13),
                                  textvariable = product_company, width= 30,)
        self.txtp_compy.grid(row=10, column = 1, sticky = W)
        
        #Add a product contect variables label
        self.labelp_cont= Label(LeftSideFrame, 
                                   font=('Times New Roman',12, 'bold'),
                                  text = 'company Contect:', padx = 2,pady=2,
                                  bg = 'ivory', fg = 'firebrick')
        self.labelp_cont.grid(row = 12, column = 0, stick =W)
        
        self.txtp_cont = Entry(LeftSideFrame, 
                                   font=('Times New Roman',13),
                                  textvariable = product_contect, width= 30,)
        self.txtp_cont.grid(row=12, column = 1, sticky = W)
        
        ###Add dummy to fill the space on left pannel
        self.labelp_dummy= Label(LeftSideFrame,bg = 'ivory')
        self.labelp_dummy.grid(row = 0, column = 0, stick =W)
        self.labelp_dummy1= Label(LeftSideFrame,bg = 'ivory')
        self.labelp_dummy1.grid(row = 1, column = 0, stick =W)
        self.labelp_dummy2= Label(LeftSideFrame,bg = 'ivory')
        self.labelp_dummy2.grid(row = 3, column = 0, stick =W)
        self.labelp_dummy3= Label(LeftSideFrame,bg = 'ivory')
        self.labelp_dummy3.grid(row = 5, column = 0, stick =W)
        self.labelp_dummy4= Label(LeftSideFrame,bg = 'ivory')
        self.labelp_dummy4.grid(row = 7, column = 0, stick =W)
        self.labelp_dummy5= Label(LeftSideFrame,bg = 'ivory')
        self.labelp_dummy5.grid(row = 9, column = 0, stick =W)
        self.labelp_dummy6= Label(LeftSideFrame,bg = 'ivory')
        self.labelp_dummy6.grid(row = 11, column = 0, stick =W)
        self.labelp_dummy7= Label(LeftSideFrame,bg = 'ivory')
        self.labelp_dummy7.grid(row = 13, column = 0, stick =W)
        
        
        #Step 3.4 add a scorel bar in the UI
        scroll_bar = Scrollbar(RightSideFrame)
        scroll_bar.grid(row =0, column=1, sticky='ns')
        
        iteamList = Listbox(RightSideFrame, width = 40, height= 16, 
                              font=('Times New Roman',12, 'bold'),
                              yscrollcommand = scroll_bar.set)
        
        #Above created product list from init module
        iteamList.bind('<<ListboxSelect>>',product_reco)
        iteamList.grid(row = 0, column=0, padx = 8)
        scroll_bar.config(command = iteamList.yview)
        
###########################################################################
        
        #Step 4 Add a butten to the operating frame
        #Insert button
        self.buttonInsert = Button(OperatingFrame, text = 'Data Insert',
                                  font= ('Times New Roman',12),
                                  height = 1, width= '10', bd = 4,
                                  command=sav_data)
        self.buttonInsert.grid(row = 0, column = 0)
        
        #Product infor button
        self.buttoninfo = Button(OperatingFrame, text = 'Product info',
                                  font= ('Times New Roman',12),
                                  height = 1, width= '10', bd = 4,
                                  command=ShowProductList)
        self.buttoninfo.grid(row = 0, column = 2)
        
        #Reset data entry button
        self.buttonreset = Button(OperatingFrame, text='Reset Entry',
                                 font= ('Times New Roman',12),
                                  height = 1, width= '10', bd = 4, command=clear)
        self.buttonreset.grid(row = 0, column = 4)
        
        #Delet data entry button
        self.buttondel = Button(OperatingFrame, text='Delete Entry',
                                 font= ('Times New Roman',12),
                                  height = 1, width= '10', bd = 4,
                                  command=del_recod)
        self.buttondel.grid(row = 0, column = 6)
        
        #Search data entry button
        self.buttonsearch = Button(OperatingFrame, text='Search Entry',
                                 font= ('Times New Roman',12),
                                  height = 1, width= '10', bd = 4,
                                  command = search_db)
        self.buttonsearch.grid(row = 0, column = 8)
        
        #Update data entry button
        #self.buttonupdate = Button(OperatingFrame, text='Upgrade Entry',
                                 #font= ('Times New Roman',12),
                                  #height = 1, width= '10', bd = 4,)
        #self.buttonupdate.grid(row = 0, column = 10)
        
        #Update data entry button
        self.buttonclose = Button(OperatingFrame, text='Close',
                                 font= ('Times New Roman',12),
                                  height = 1, width= '10', bd = 4,
                                  command=close)
        self.buttonclose.grid(row = 0, column = 12)
        
        #Dummy button space
        self.buttondummy = LabelFrame(OperatingFrame,width= 2)
        self.buttondummy.grid(row = 0, column = 1)
        self.buttondummy2 = LabelFrame(OperatingFrame,width= 2)
        self.buttondummy2.grid(row = 0, column = 3)
        self.buttondummy3 = LabelFrame(OperatingFrame,width= 2)
        self.buttondummy3.grid(row = 0, column = 5)
        self.buttondummy4 = LabelFrame(OperatingFrame,width= 2)
        self.buttondummy4.grid(row = 0, column = 7)
        self.buttondummy5 = LabelFrame(OperatingFrame,width= 2)
        self.buttondummy5.grid(row = 0, column = 9)
        self.buttondummy6 = LabelFrame(OperatingFrame,width= 2)
        self.buttondummy6.grid(row = 0, column = 11)
        
        
###############################################################################
#Back-end database related buttons opration class
'''In this class will store all the funciton 
and the back-end operarion of every button 
and store those infoamtion into the SQL database'''

class op_database:
    '''COnnection with the database'''
    def connection(self):
        print('Databased: Connection needed')
        #Store the databased into new variable
        conn = sqlite3.connect('inventory.db')
        #Feature and backend function of the curser is added
        curs = conn.cursor()
        query = "create table if not exists product (pid integer primary key,\
        pname text, price text, qty text,company text, contact text)"
        curs.execute(query)
        conn.commit()
        conn.close()
        print('Database : Connection process is completed\n')
        
    #insert operation of the vrious datapoints
    def insert(self,pid,name,price,qty,compny,contact):
        print("Databse: Insert operation processed")
        conn = sqlite3.connect('inventory.db')
        #Feature and backend function of the curser is added
        curs = conn.cursor()
        query = "insert into product values(?,?,?,?,?,?)"
        curs.execute(query,(pid,name,price,qty,compny,contact))
        conn.commit()
        conn.close()
        print("Database: Loading process is completed\n")
        
    #funciton for the display the database into the system
    def display(self):
        print("Database: Display the database")
        conn = sqlite3.connect('inventory.db')
        #Feature and backend function of the curser is added
        curs = conn.cursor()
        query = "Select * from product"
        curs.execute(query)
        rows= curs.fetchall()
        conn.close()
        print('Database: Disply  the database process is completed\n')
        return rows
    
    #Create a funciton for the delet button to del the dataset from repo
    def delt(self,pid):
        print("Database: Display the database")
        conn = sqlite3.connect('inventory.db')
        #Feature and backend function of the curser is added
        curs = conn.cursor()
        curs.execute('delete from product where pid=?',(pid,))
        conn.commit()
        conn.close()
        print(pid,'Database:Delete method finished\n')
       
    #create a funciton for the search button
    def search_butt(self,pid='',name='', price='',qty='', 
                    company='', contect=''):
        print('Database: Search funciton exicution')
        conn= sqlite3.connect('inventory.db')
        curs = conn.cursor()
        curs.execute("select * from product where pid = ? or \
                     pname=? or price=? or qty=? or company=? or contact=?",
                     (pid,name,price,qty,company,contect))
        rows = curs.fetchall()
        conn.close()
        print(pid,'Database: Search process is completed\n')
        return rows
    

        
        
        
        
        
#Load the UI into the system
if __name__ =='__main__':
    root=Tk()
    application = product_ui(root)
    root.mainloop()