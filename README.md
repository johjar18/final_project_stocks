# final_project_stocks# final_project_stock
For my project, I created a database that houses information about stocks. There are two tables in the database: Stocks- which provides some general information about the particular stock (current price, previous day's price, etc) and Overview- which gives some context such as the stock exchange the stock is traded on as well as which industries/sectors it belongs to. Both tables were populated from three web-scraped tabs (Summary, Profile, and Financials) from that particular stock's page on Yahoo' Finance.

At the beginning of the program, the user will be prompted to enter in a stock symbol. The code is structured around each symbol being created as an instance, and from that point onward, all relevant information for the symbol can be scraped from Yahoo Finance. The program will continue so long as a user inputs a valid symbol.

I used Falcon in tandem with plotly to display the stock information in the table. When you've completed your search for stocks, enter exit when prompted, and another prompt will ask you if you want to view a chart. If you enter 'Yes',there will be four options for you to display. For this option, it is especially important that you have the Falcon client downloaded so that you will be connected to my database (which has already been pushed to GitHub).

That's about it! I've enjoyed this semester and I hope you enjoy the program!

