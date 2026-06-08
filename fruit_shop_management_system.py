def inventory():#------------------------------------------------------------------------------------------->>>Inventory of the store
    print(' '*27,'INVENTORY')
    print('-'*68)
    print('Item         Quantity(KG)        Actual price(Rs)      Selling price(Rs)')
    print('-'*68)
    for i in range(0,len(fruits)):
        print(fruits[i],' '*8,Quantity[i],' '*15,Actual_price[i],' '*17,Selling_price[i])
    print('-'*68)
def Store_inventory():
    print(' '*10,'_'*9)
    print(' '*10,'INVENTORY')#------------------------------------------------------->>inventory for customer to see availability of fruits
    print('_'*37)
    print('Quantity       Item(price/KG)')
    print('_'*37)
    for i in range(0,len(fruits)):
        print(' ',Quantity[i],'KGs',' '*9,fruits[i],'(',Selling_price[i],'rs/KG',')',sep='')                 
    print('_'*37)
    print()
def customer_cart():#---------------------------------------------------------------------------------->>customer cart
    for i in range(0,len(fruits_cart)):
        print(quantity_cart[i],'KGs of ',fruits_cart[i],sep='')
    print('These items available in your cart')
print('_'*60)
print('*'*12,"Welcome to the vijay's Fruit Shop",'*'*12)
print('_'*60)
print('Who are you..?')
fruits=['orange','mango','banana','apple','liche','grape','guava','cherry','papaya','kiwi']
Quantity=[15,20,40,30,20,20,25,22,50,30]#quantity in store
Actual_price=[45,65,50,110,80,45,60,120,70,250]
Selling_price=[60,80,70,130,100,60,80,150,100,300]
fruits_cart=[]#fruits in cart
quantity_cart=[]#quantity in cart
price_cart=[]
profit_cart=[]
total_bill=0
profit=0
while True:
    print('1.Shopkeeper','\n2.Customer','\n3.Exit')
    ask=input('Choose any option that suits you :')
    print('_'*60)
    #------------------------------------------------------------------------------------------------------------------------------>>>>shopkeeper access
    if ask=='1':
        
        ask=input('enter your id :')
        pas=input('enter your password :')
        if ask=='admin' and pas=='admin':
            print('Current available fruits in the store are :')
            inventory()
            while True:
                print('1.Add Items','\n2.Remove Items','\n3.Total Profit','\n4.Exit')
                ask=input('Choose any option :')
                print('-'*30)
                if ask=='1':#----------------------------------------------------------------------------------------->>add items
                    
                        item=input('Enter item name :')
                        try:
                            quantity=int(input('How many items to be added in the store :'))
                        except:
                            print('Enter valid quantity')
                            continue
                        if item not in fruits:
                            actual_price=int(input('Enter the Actual price of the item :'))
                            selling_price=int(input('Enter the Selling price of the item :'))
                            fruits.append(item)
                            Quantity.append(quantity)
                            Actual_price.append(actual_price)
                            Selling_price.append(selling_price)
                            print(quantity,'KGs of ',item,'s added successfully to the store',sep='')
                        else :
                            i=fruits.index(item)
                            Quantity[i]+=quantity
                            print(quantity,'KGs of ',item,'s added successfully to the store',sep='')
                        inventory()             
                        
                elif ask=='2':#----------------------------------------------------------------------------------------->>remove items
                    item=input('Enter which fruit to remove :')
                    if item in fruits :
                        try:
                            quant=int(input('How many items you have to remove :'))
                        except:
                            print('Enter valid quantity')
                        i=fruits.index(item)
                        if quant>Quantity[i]:
                            print("You don't have",quant,item,'in the Inventory')                        
                        if Quantity[i]==quant:
                            fruits.pop(i)
                            Quantity.pop(i)
                            Actual_price.pop(i)
                            Selling_price.pop(i)
                            inventory()
                            print('The ',item,'s Successfully removed from your Inventory','\n',sep='')
                        elif quant<Quantity[i]:
                            Quantity[i]-=quant
                            print(quant,' ',item,'s Successfully removed from your Inventory','\n',sep='')
                            inventory()
                    else:
                        print("This item is not there in your store, Don't worry")
                
                elif ask=='3':#----------------------------------------------------------------------------------------->>profit 
                    
                    print('Profit for each item is :')
                    for i in range(len(fruits)): 
                        profit_x=Selling_price[i]-Actual_price[i]
                        print(profit_x,'.Rs. for',' ',fruits[i],sep='')
                    print(' '*30,'-'*10)
                    print('Total profit for the inventory is :',profit)
                    print(' '*30,'-'*10)
                    print('***')
                    print()
                elif ask=='4':#------------------------------------------------------------------------------------------->>exit
                    break
                else:
                    print('Choose the option from above')
        else:
            print('wrong ID or Password,.Please try again.!')
            print()
        print('-'*15)
    elif ask=='2':#----------------------------------------------------------------------------------------------------------------------------------------->>>>>customer access
        name=input('Please enter your Name :')
        while True:
            mobile_number=input('Enter your mobile number :')
            if len(mobile_number)!=10 or not mobile_number.isdigit():
                print('Not a valid number')
            else:
                break
        Store_inventory()      
        while True:
            print('1.Add items to cart','\n2.Remove items from cart','\n3.Do you want to buy items in the cart','\n4.Cart')
            ask=input('Choose one option from above :')
            if ask =='1':#---------------------------------------------------------------------------------------->>add items in cart
                    Store_inventory()#------------------------------------------------------->inventory after adding item into cart
                    item=input('Enter which fruit to add to the cart :')
                    if item in fruits:
                        
                        if item not in fruits_cart:
                            try:
                                quant=int(input("Enter how many items Do you want :"))
                            except:
                                print('Enter valid quantity')
                                continue
                            i=fruits.index(item)
                            if quant<=Quantity[i]:#-------------------------------------------------------------------->logic to add fruits in cart
                                fruits_cart.append(fruits[i])
                                quantity_cart.append(quant)
                                price_cart.append(Selling_price[i]*quant)
                                j=fruits_cart.index(item)
                                Quantity[i]-=quant
                                print()
                                print(quant,'KGs of ',item,'s added to your cart and cost is ',price_cart[j],sep='')
                            else:
                                print('we have only ',Quantity[i],'KGs of ',item,sep='')
                                print()
                        elif item in fruits_cart:
                            try:
                                quant=int(input("Enter how many items Do you want :"))
                            except:
                                print('Enter valid quantity')
                                continue
                            i=fruits.index(item)
                            if quant<=Quantity[i]:
                                j=fruits_cart.index(item)
                                quantity_cart[j]+=quant
                                Quantity[i] -= quant
                                price_cart[j]+=(Selling_price[i]*quant)
                                print(quantity_cart[j],' ',item,'s added to your cart and cost is ',price_cart[j],sep='')
                            else:
                                print('we have only ',Quantity[i],'KGs of ',item,sep='')                            
                        elif Quantity[i]==0 or quant>Quantity[i]: 
                            print('we have ',Quantity[i],'KGs of ',item,'\n So choose less than ',Quantity[i],'KGs',sep='')
                            print()
                        
                    else:
                        print("We don't have",item,'\nPlease kindy choose another fruits from the store','\n')
            elif ask=='2':#-------------------------------------------------------------------------------------------------->>remove items from cart
                customer_cart()
                item=input('Enter which fruit to remove :')
                if item in fruits_cart:
                    store_profit=0
                    try:
                        quant=int(input("Enter how many items Do you want :"))
                    except:
                        print('Enter valid quantity')
                        continue
                    i=fruits_cart.index(item)
                    if quant>quantity_cart[i]:
                        print("You don't have",quant,item,'in your cart')
                    elif quant==quantity_cart[i]:
                        i=fruits_cart.index(item)
                        j=fruits.index(item)
                        Quantity[j]=Quantity[j]+quantity_cart[i]
                        fruits_cart.remove(item)
                        price_cart.pop(i)
                        quantity_cart.pop(i)
                        print()
                        print(item,'is removed from your cart')
                        for i in range(0,len(fruits_cart)):
                            print(quantity_cart[i],'KGs of ',fruits_cart[i],sep='')
                        print()
                        print('Available in your cart')
                    elif quant<quantity_cart[i]:
                        j=fruits.index(item)
                        quantity_cart[i]-=quant
                        Quantity[j]+=quant
                        price_cart[i]-=(Selling_price[j]*quant)
                        print(quant,' ',item,'s removed from your cart',sep='')                            
                elif item not in fruits_cart:
                    print('The',item,'is not in your cart')
            
            elif ask=='3':#----------------------------------------------------------------------------------->Billing
                #--------------------------------------------------------------------------------------------->Profit Calculation
                profit=0
                for i in range(len(fruits_cart)):
                    j=fruits.index(fruits_cart[i])
                    profit+=(Selling_price[j]-Actual_price[j])*quantity_cart[i]
                print('_'*25)
                print(' '*9,'BILL')
                print('_'*25)
                print('Customer name :',name,'\nMobile number :',mobile_number)
                print('-'*20)
                print('Items        price |')
                print('-'*20)
                total_bill=0
                for i in range(len(fruits_cart)):
                    total_bill+=price_cart[i]
                    print(fruits_cart[i],'        ',price_cart[i])
                print('_'*25)
                print('TOTAL BILL =',total_bill,'Rs.')
                print('DISCOUNT   =','10%')
                print('Bill To Pay==>',total_bill-total_bill*0.1)
                print('**You got complimentory discount of 10%**')
                print('_'*25)
                
                print('Thank..YOU..FOR SHOPPING WITH US','\nSee You Again...BYE...')
                print('''
''')
                fruits_cart.clear()
                quantity_cart.clear()
                price_cart.clear()
                break
            elif ask=='4':#---------------------------------------------------------------------------------->Cart
                print()
                total_bill=0
                print(' '*10,'CART')
                print('_'*30)
                print('Items             Total price')
                print('-'*30)
                for i in range(len(fruits_cart)):
                    print(fruits_cart[i],'          ',price_cart[i],'rs for ',quantity_cart[i],' units',sep='')
                for i in range(len(fruits_cart)):
                    total_bill+=price_cart[i]
                print('_'*30)
                print('Total',' '*17,total_bill,'rs',sep='')                
                print('-'*30)
            elif ask=='5':
                print(5)
            elif ask=='6':
                print(6)
            else:
                print('choose a valid option')
        
    elif ask=='3':
        break
    else:
        print('Choose a valid option')
        print()
