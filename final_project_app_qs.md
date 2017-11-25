# SI 364 - Final Project questions

## Overall

* **What's a one-two sentence description of what your app will do?**
The app will be a record store so that I can have an excuse to catalog my collection.

## The Data

* **What data will your app use? From where will you get it? (e.g. scraping a site? what site? -- careful not to run it too much. An API? Which API?)**
I may use Discogs API through their Python client as I intend to format my csv inventory import tool to mirror their user collection format. https://github.com/discogs/discogs_client  I would probably use this to grab artist info for each product page.

* **What data will a user need to enter into a form?**
There will be two types of user - an administrator that adds and removes inventory and a shopper.
The shopper will only need to enter an email and a password.
The administrator will have the option to add inventory by manually entering all fields - Artist, catalog number, label, album title, release year, condition, notes, price - OR they may choose to do a bulk insert by uploading a properly formatted csv.

* **How many fields will your form have? What's an example of some data user might enter into it?**
Artist, catalog number, label, album title, release year, condition, notes, price
Madonna, 9 25157-1, SIRE, Like A Virgin, 1984, VG+, white vinyl dj promo, 75.00

* **After a user enters data into the form, what happens? Does that data help a user search for more data? Does that data get saved in a database? Does that determine what already-saved data the user should see?**
The data will be commited to a product table in a database. I may choose to direct the user to a page showing all entries by the artist just commited so that they may check to see that there aren't duplicate records. Since conditions vary, each row will represent a unique physical product, so inventory numbers are either 1 or 0. 

* **What models will you have in your application?**
User, Product, Sales_Order

* **What fields will each model have?**
User(id, email, password)
Product(id, artist, catalog number, label, album title, release year, condition, notes, price)
Sales_Order(id, User.id, line_id, Product.id, Product.price)

* **What uniqueness constraints will there be on each table? (e.g. can't add a song with the same title as an existing song)**
In the User table, email will be unique as it is inherently unique and id will be unique. 
In the Product table, nothing will be unique since there may be multiple entries of the same record.
In Sales_Order, id will be unique

* **What relationships will exist between the tables? What's a 1:many relationship between? What about a many:many relationship?**

* **How many get_or_create functions will you need? In what order will you invoke them? Which one will need to invoke at least one of the others?**

## The Pages

* **How many pages (routes) will your application have?**

* **How many different views will a user be able to see, NOT counting errors?**

* **Basically, what will a user see on each page / at each route? Will it change depending on something else -- e.g. they see a form if they haven't submitted anything, but they see a list of things if they have?**

## Extras

* **Why might your application send email?**

* **If you plan to have user accounts, what information will be specific to a user account? What can you only see if you're logged in? What will you see if you're not logged in -- anything?**

* **What are your biggest concerns about the process of building this application?**
