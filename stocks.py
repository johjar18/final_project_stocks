import requests
import sqlite3
from bs4 import BeautifulSoup
import sys
import json
import webbrowser


DBNAME = 'stockinfo.db'
baseurl= 'https://finance.yahoo.com/quote/'
html= requests.get(baseurl).text
soup = BeautifulSoup(html, 'html.parser')
# soup.prettify()

CACHE_FNAME = 'cache.json'
try:
    cache_file = open(CACHE_FNAME, 'r')
    cache_contents = cache_file.read()
    CACHE_DICTION = json.loads(cache_contents)
    cache_file.close()

# if there was no file, no worries. There will be soon!
except:
    CACHE_DICTION = {}
def make_request_using_cache(url):
    unique_ident = url

    ## first, look in the cache to see if we already have this data
    if unique_ident in CACHE_DICTION:
        print("GETTING CACHED DATA)")
        return CACHE_DICTION[unique_ident]

    ## if not, fetch the data afresh, add it to the cache,
    ## then write the cache to file
    else:
        # Make the request and cache the new data
        print("Making a request for new data..... MAY TAKE A WHILE")
        resp = requests.get(url)
        CACHE_DICTION[unique_ident] = resp.text
        dumped_json_cache = json.dumps(CACHE_DICTION)
        fw = open(CACHE_FNAME,"w")
        fw.write(dumped_json_cache)
        fw.close() # Close the open file
        return CACHE_DICTION[unique_ident]

# test_span=soup.find('span').text.strip()
class Symbol:
    def __init__(self, stock_symbol):
        try:

            parameters= baseurl +str(stock_symbol) +'?p=' +str(stock_symbol)
            # print(baseurl)
            # print(stock_symbol)
            # print(parameters)

            # print(parameters)
            make_request=make_request_using_cache(parameters)
            # print(make_request)
            self.name_stock= stock_symbol
            page_soup= BeautifulSoup(make_request, 'html.parser')
            symbol_soup= page_soup.find('h1').text.strip()
            list_symbol=[]
            for i in symbol_soup.split():
                list_symbol.append(i)
            stock_symbol=list_symbol[0]
            # print(stock_symbol)
            # print('a')
            self.stock_symbol= stock_symbol

        except:
            self.stock_symbol=None
            print("Error! Symbol couldn't be found! System will now shut down...")

            sys.exit()




            # print(

        # _________________________________________
        try:
            parameters=baseurl +str(stock_symbol) +'/history?p=' +str(stock_symbol)
            make_request= make_request_using_cache(parameters)
            page_soup= BeautifulSoup(make_request, 'html.parser')
            previous_price_soup=page_soup.find_all(attrs={'data-reactid': 76})
        #     # print('e')
            # print(previous_price_soup)# RETURNS PREVIOUS PRICE :)
            for item in previous_price_soup:
                concatenate_price_previous= "$"+item.text.strip()
                # print(concatenate_price_previous)
            self.previous_price= concatenate_price_previous

            # print(self.previous_price)
        #     # list_current_prices=[]
        #     # list_item=[]
        #     # for item in current_price_soup:
        #     #     list_item.append(item.text.strip()[1][1])
        #     #     # print(list_item)
        #     #     print(list_item)
        #
        #
        #     #         list_current_prices.append(item)
        #     #
        #             # print(item.text.strip())
        #         #     print(list_current_prices)
        #         # print(current_price_soup)
        except:
            self.previous_price=None
            pass

        try:
            parameters=baseurl +str(stock_symbol) +'/history?p=' +str(stock_symbol)
            make_request= make_request_using_cache(parameters)
            page_soup= BeautifulSoup(make_request, 'html.parser')
            current_price_soup=page_soup.find_all(attrs={'data-reactid':61})
            # print(last_price_soup)
            for item in current_price_soup:
                current_price= item.text.strip()
                concatenate_price= "$"+current_price
                # print(concatenate_price)
            # print(current_price) #WORKS!!!
            self.current_price= concatenate_price

        except:
            self.current_price=None
            pass
            # print("Error! Symbol doesn't exist!")


        try:
            parameters=baseurl +str(stock_symbol) +'/history?p=' +str(stock_symbol)
            make_request= make_request_using_cache(parameters)
            page_soup= BeautifulSoup(make_request, 'html.parser')
            high_price_soup=page_soup.find_all(attrs={'data-reactid':55})[0].text.strip()
            # print(high_price_soup)

            # # print(self.previous_price)
            # subtraction= (float(self.current_price))-(float(self.previous_price))
            # division= (subtraction)/float(self.previous_price)
            # times_hundred= division *100
            # string_hundred= str(round(times_hundred,2))
            # concatention=string_hundred +"%"
            # print(concatention)
            # print(division)
            # print(subtraction)
            self.highest_price="$"+high_price_soup



        except:
            self.highest_price=None


        try:
            parameters= baseurl +str(stock_symbol)+'?p=' +str(stock_symbol)
            make_request= make_request_using_cache(parameters)
            page_soup= BeautifulSoup(make_request, 'html.parser')
            exchange_soup=page_soup.find_all('span',attrs={'data-reactid':9})[0].text.strip()

            # print(exchange_soup)

            self.exchange=exchange_soup

        except:
            self.exchange=None


        try:
            parameters= baseurl +str(stock_symbol)+'?p=' +str(stock_symbol)
            make_request= make_request_using_cache(parameters)
            page_soup= BeautifulSoup(make_request, 'html.parser')
            year_soup=page_soup.find_all(attrs={'data-reactid':100})[0].text.strip()
            # print(year_soup)
            self.year_estimate= "$" + year_soup
             # for item in year_soup:
            #     print(item.text.strip)
            try:
                parameters= baseurl +str(stock_symbol)+'?p=' +str(stock_symbol)
                make_request= make_request_using_cache(parameters)
                page_soup= BeautifulSoup(make_request, 'html.parser')
                year_soup=page_soup.find_all(attrs={'data-reactid':96})[0].text.strip()
                # print(year_soup)


            except:
                self.year_estimate=None
                pass



        except:
            self.year_estimate=None
            pass

        try:
            parameters= baseurl +str(stock_symbol)+'?p=' +str(stock_symbol)
            make_request= make_request_using_cache(parameters)
            page_soup= BeautifulSoup(make_request, 'html.parser')
            name_soup=page_soup.find('h1').text.strip()
            # print(name_soup)
            self.name_stock= name_soup

        except:
            self.name_stock=None
            pass

        try:
            # https://finance.yahoo.com/quote/GOOG/financials?p=GOOG
            parameters= baseurl +str(stock_symbol) +'/financials?p=' +str(stock_symbol)
            make_request= make_request_using_cache(parameters)
            # print(make_request)
            page_soup= BeautifulSoup(make_request, 'html.parser')
            revenue_soup=page_soup.find_all(attrs={'data-reactid': 42})[1].text.strip()
            # print(revenue_soup)
            self.revenue= "$" + revenue_soup

        except:
            self.revenue=None
            pass

        try:
            parameters= baseurl +str(stock_symbol) +'/profile?p=' +str(stock_symbol)
            make_request= make_request_using_cache(parameters)
            page_soup= BeautifulSoup(make_request, 'html.parser')
            industry_soup=page_soup.find_all('strong',attrs={'data-reactid': 25})
            # print(industry_soup)

            if len(industry_soup)==0:
                alt_industry_soup= page_soup.find_all('strong', attrs={'data-reactid':27})[0].text.strip()
                # print(alt_industry_soup)
                self.industry= alt_industry_soup
            else:
                # print(industry_soup)
                self.industry= industry_soup[0].text.strip()
                # print('a')
        except:
            self.industry= None
            # print('b')





            # pass
            # print(self.industry)

        try:
            parameters= baseurl +str(stock_symbol) +'/profile?p=' +str(stock_symbol)
            make_request= make_request_using_cache(parameters)
            page_soup= BeautifulSoup(make_request, 'html.parser')
            sector_soup=page_soup.find('strong').text.strip()
            # print(sector_soup)
            self.sector= sector_soup

        except:
            self.sector=None
            pass






        # self.stock_symbol= stock_symbol
        # self.current_price= current_price
        # self.last_price= last_price
        # self.change= times_hundred
        # self.year_estimate= year_estimate
        # self.name_stock= name_stock
        # self.exchange= exchange
        # self.revenue= revenue
        # self.gross_profit= gross_profit
        # self.sector= sector
    # # def __str__(self):
    #     return "{}".format(self.stock_symbol)

    # def search_symbol(self,stock_symbol):
    #     return self.stock_symbol

        #     return '{}'.format(self.stock_symbol)
        #
        # except:
        #     return "Error! Symbol doesn't exist!"

    # def __str__():
    #     return " "



    # def search_last_price(self):
    #
    # # -------------------------------------------#


# def create_database(attributes):
        try:
            conn = sqlite3.connect(DBNAME)
            cur = conn.cursor()
        except Error as e:
            print(e)
        print('Inserting Data.')

        prompt= input("Stock Table exists. Delete? Yes or No")
        if prompt.upper()=="YES":
            cur.execute("DROP TABLE IF EXISTS 'Stock'")
            conn.commit()

        else:

            stock_table = '''
                CREATE TABLE IF NOT EXISTS 'Stock' (
                    'Id' INTEGER PRIMARY KEY,
                    'Symbol' TEXT NOT NULL,
                    'CurrentPrice' TEXT NOT NULL,
                    'PreviousPrice' TEXT NOT NULL,
                    'HighestPrice' TEXT NOT NULL,
                    '1-yearTargetEstimate' TEXT NOT NULL
                    );
            '''
            cur.execute(stock_table)
            conn.commit()




            insertion=(None, self.stock_symbol, self.current_price, self.previous_price, self.highest_price, self.year_estimate)
            stock_table = 'INSERT OR IGNORE INTO "Stock" '
            stock_table += 'VALUES (?, ?, ?, ?, ?, ?)'
            cur.execute(stock_table, insertion)
            conn.commit()

        prompt= input("Overview table exists. Delete? Yes or No")
        if prompt.upper()=="YES":

            cur.execute("DROP TABLE IF EXISTS 'Overview'")
            conn.commit()

        else:
            overview_table = '''
                CREATE TABLE IF NOT EXISTS 'Overview' (
                    'StockName' TEXT PRIMARY KEY NOT NULL,
                    'Exchange' TEXT,
                    'TotalRevenue' TEXT,
                    'Industry' TEXT,
                    'Sector' TEXT
                    );
            '''
            cur.execute(overview_table)
            conn.commit()


            insertion=(self.name_stock, self.exchange, self.revenue, self.industry, self.sector)
            overview_table = 'INSERT OR IGNORE INTO "Overview" '
            overview_table += 'VALUES (?, ?, ?, ?, ?)'

            cur.execute(overview_table, insertion)
            conn.commit()
        # # #
            query = "SELECT * FROM Stock"
            overview_query= "SELECT * FROM Overview"
            cur.execute(query)
            # cur.execute(overview_query)

            stock_mapping = {}
            #
            for stock in cur:
                stock_mapping[self.stock_symbol] = self.name_stock
        # # #
        # #     cur.execute(overview_query)
        # #     # overview_mapping= {}
        #     for item in cur:
        #         stock_name= item[0]
        #         stock_mapping[stock_name]= symbol
        # #     #


# def insert_data(attributes):
    # pass


#
# def make_stock_request():
        #BUILD IN TRY & EXCEPT LATER

        # test_table= soup.find('table', class_='W(100%) M(0) Bdcl(c)')
        # print(make_request)
        # test_span=soup.find('span', data=>reactid='49').text.strip()
        # if test_span=='Please check your spelling. Try our suggested matches or see results in other tabs.':
        #     print("That symbol is not valid! Please enter a valid symbol!")

# def find_stock_attributes():






    # print(symbol) #RETURNS DESIRED OUTPUT
    # RETURN TO CODE TO ALLOW USER TO CONTINUE INPUTTING SYMBOLS UNTIL 'EXIT'



# make_stock_request()
# find_stock_attributes()
# create_database()
#
# create_database(DBNAME)

if __name__ == "__main__":
    #GOT THIS PART WORKING WOO WOO!

    stock_symbol= ' '
    while stock_symbol.upper()!='EXIT':
        stock_symbol=input("Please enter a valid stock symbol or 'exit' to quit: ").upper()

        if stock_symbol.upper()=="EXIT":
            print("You will now be asked chart stuff...")
            break
        else:
            attributes=Symbol(stock_symbol)

    chart= ' '
    while chart.upper()!="NO":
        chart= input("Would you like to see a chart? Yes/No ")

        if chart.upper()== "YES":
            chart= input("Select one of the following: exchange, industry, sector, CurrentPrice")
            if chart.upper()=='EXCHANGE':
                webbrowser.open('https://plot.ly/~johjar/18/')
            elif chart.upper()=='INDUSTRY':
                webbrowser.open('https://plot.ly/~johjar/14/')
            elif chart.upper()=='SECTOR':
                webbrowser.open('https://plot.ly/~johjar/16/')
            elif chart.upper()=='CURRENTPRICE':
                webbrowser.open('https://plot.ly/~johjar/12/')
            else:
                print('Please enter a valid chart command')
                # print(chart)
        if chart.upper()=='NO':
            print("Goodbye (again)!")
            break
        # else:
        #     continue

        # create_database(attributes)
            # print(attributes)
            # attributes=search_last_price(symbol)
