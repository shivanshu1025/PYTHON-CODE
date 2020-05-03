from util import *
c=connection()
cur=connection.con.cursor()
class table:
    def __init__(self):
        q="create table TBL_STOCK(Product_Id varchar(6) primary key, Product_Name varchar(20),Quantity_On_Hand number(30),Product_Unit_Price number(30) ,ReOrder_Level number(30))"
        q1="create table TBL_SALES(Sales_Id varchar(8), Sales_date varchar(10),Product_Id varchar(8), Quantity_Sold number(30),Sales_Price_Per_Unit number(30),primary key(Sales_ID),foreign key(Product_ID) references TBL_STOCK(Product_ID),unique(Product_ID))"
        try:
            cur.execute(q)
            cur.execute(q1)
            print('table created')
            connection.con.commit()
        except:
            print('already created')
class insert():
    def __init__(self):
        q="""insert into TBL_STOCK values('%s','%s',%d,%d,%d)"""
        q1="""insert into TBL_SALES values('%s','%d','%s',%d,%d)"""
        while True:
            choice=input('do you want to enter the record y/n')
            if choice=='y':
              try:
                Product_ID=input('Product_ID ')
                Product_Name=input('Product_Name ')
                Quantity_On_Hand=int(input('Quauntity_On_Hand '))
                Product_Unit_Price=int(input('Product_Unit_Price '))
                ReOrder_Level=int(input('ReOrder_Level '))
                Sales_ID=input('Sales_ID ')
                Sales_Date=int(input('Sales_Date '))
                Product_ID=input('Product_ID ')
                Quantity_Sold=int(input('Quantity_Sold '))
                Sales_Price_Per_Unit=int(input('Sales_Price_Per_Unit '))
                cur.execute(q%(Product_ID,Product_Name,Quantity_On_Hand,Product_Unit_Price,ReOrder_Level))
                cur.execute(q1%(Sales_ID,Sales_Date,Product_ID,Quantity_Sold,Sales_Price_Per_Unit))
                connection.con.commit()
              except:
                  print('EXCEPTION HANDLING ')
            else:
                break
        
class select:
    def __init__(self):
        q='select * from TBL_STOCK'
        q1='select * from TBL_SALES'
        cur.execute(q)
        records=cur.fetchall()
        print('...............TBL_STOCK............. ')
        for row in records:
            print('Product_ID= ',row[0])
            print('Product_Name =',row[1])
            print('Quantity_On_Hand= ',row[2])
            print('Product_Unit_Price= ',row[3])
            print('ReOrder_Level= ',row[4])
        cur.execute(q1)
        records=cur.fetchall()
        print('...............TBL_SALES............. ')
        for row in records:
            print('Sales_ID= ',row[0]) 
            print('Sales_Date= ',row[1])
            print('Product_ID= ',row[2])
            print('Quantity_Sold= ',row[3])
            print('Sales_Price_Per_Unit= ',row[4])
        
class delete():
    def __init__(self):
        print('ENTER THE TABLE FROM WHICH YOU WANT TO DELETE THE RECORDS ')
        choice=int(input('0 for TBL_STOCK / 1 FOR TBL_SALES '))
        if choice==0:
            try:
                id=input('enter the id for record ')
                q='delete TBL_STOCK where id=%s'
                cur.execute(q%id)
                connection.con.commit()
                print('RECORD DELETED ')
            except:
                print('delete its corresponding entry from TBL_SALES first ')
        else:
            try:
                id=input('enter the id for record ')
                q='delete TBL_SALES where Product_ID=%s'
                cur.execute(q%id)
                connection.con.commit()
                print('RECORD DELETED ')
            except:
                print('NO RECORDS FOR THIS ID ')
            
class profit():
    def __init__(self):
        try:
            id=input('enter the product_id ')
            q="select Quantity_On_Hand from TBL_STOCK where Product_ID ='%s'"
            q1="select Product_Unit_Price from TBL_STOCK where Product_ID ='%s'"
            cur.execute(q%id)
            quantity=cur.fetchall()
            cur.execute(q1%id)
            productPrice=cur.fetchall()
            print(quantity)
            print(productPrice)
            Quantity=quantity[0][0]
            PRICE=productPrice[0][0]
            COST_PRICE=Quantity*PRICE
            print(COST_PRICE)
            q="select Quantity_Sold from TBL_SALES where Product_ID ='%s'"
            q1="select Sales_Price_Per_Unit from TBL_SALES where Product_ID ='%s'"
            cur.execute(q%id)
            SALE=cur.fetchall()
            cur.execute(q1%id)
            SalePrice=cur.fetchall()
            Quantity=int(SALE[0][0])
            PRICE=int(SalePrice[0][0])
            SELLING_PRICE=Quantity*PRICE
            print(SELLING_PRICE)
            PROFIT=COST_PRICE-SELLING_PRICE
            print('YOUR PROFIT IS ',PROFIT)
            
        except:
            print('NO PRODUCT FOR THIS ID')            


        

