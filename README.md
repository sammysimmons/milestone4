# Personal Advertising/ Design services Project-MS4
design services and portfolio for educational purposes only, which i wish to expand upon marking completion. bootstrap styling template has been used for this project.

Milestone 4 can be accesses here:
insert heroku link https://milestone-4-samsimmons.herokuapp.com/


## UX & UI
both desktop and mobile friendly, landing on the homepage you have an intro, breif overview of who i am, and the skills i could offer with 3 select services that are standard packages. The aim with this website is for further advertisement and for me to gain more freelance on completion of my course whether this be graphic design or more front end developement. 

The design is based around being clean and concise for usability, as the main focus of the site, utilising the styling template bootstrap.

### Wireframe
 my Wireframes can be viewed [here](https://xd.adobe.com/view/0cbb6ccf-98f5-478b-bfce-4eb560d51a17-59e8/)


## Technologies Used

Figma - To create a wireframe
Lucid Chart - To create the Entity Relationship Diagram (ERD)
HTML - To create the basics
CSS - To improve placements and design
JavaScript - The engine to create user interaction
Python - Programming language
Postgres - Opensource database to save the transactions, profile, and orders
Django - Web framework in python
Bootstrap - To make the design responsive
Font Awesome - Easy icon access for the icons
Font Awesome animations - Additional animations for the Font Awesome icons
GitHub Wiki TOC generator - Generates a MarkDown TOC online
JavaScript Libraries
jQuery - To improve input field feedback
flatpickr - lightweight, powerful JavaScript datetimepicker with no dependencies
DataTables - Adds advanced interaction controls to HTML tables
Stripe - For credit card transactions
Python & Django Libraries
pillow - Python Imaging Library
Stripe - Credit card payments and transaction security
boto3 - To connect to AWS
django-allauth - Authentication, registration & account management
django-countries - Provides country choices for use with forms
django-phonenumber-field - A Django library which interfaces with python-phonenumbers to validate
django-crispy-forms - Controls the rendering behaviour of Django forms
django-filter - Easy searching and filtering query sets

## User stories

1) "Sam designs has alot of potential especially for the level of services she could offer, be great if you expand more in depth into your portfolio and what each project/ piece entailed"

2) "I typically go agency based for anything we need design or developement wise, but having someone who could turn things around faster and who could get to know our brand on a different level would be great"

As a user, I want to easily fill in the forms for a service request (services)
As a user, I want to upload my artwork fast and easy in the same system (checkout form)
As a user, I want a secured overview of my order history (dashboard)
As a user, I do not want to fill in my details every time, but do want to change them if needed (profile)
As an employee, I want to know which service are required per order (order)
As an employee, I want to change the status of an order (admin list actions)
As an employee, I would like to download the artwork (order details)
As an employee, I would like to upload and overwrite the artwork (order details)
As an employee, I want to search and filter the orders (search & filter)

## Strategy

As the target audience is broad for design and development services, I have kept the interface clean and ease of navigation. Users can quickly look through available services, or even search for what they may require, on the services page you can request a tailored quote as no job is the same when it comes to development or design, each enquiry can vary from dependent on the company. So the direction i took with the service page is for clients to complete a form in which i could check my schedule and quote appropriately for what they require.

## Structure

Responsiveness and clarity were my goal for this site. It is not feature heavy because I don't want to over complicate something that should be simple.

## Features

This project is built with Python, Django, CSS, bootstrap, and uses Django to store user data. I chose to use bootstrap to keep a nice, clean grid feel to the site.

- service blocks -  users can easily see and scroll through service which are displayed in a card block formats, and then complete a form tailoring theyre service requirements

- Login - Users have the ability to create an account, which for future purposes could turn into a client portal for accessing and downloading their workable files from

- Imagery - All imagery is from my portfolio which i have permission to use from each of the brands, aslong as the products are already in the public eye.

## Future Features
-My design career extends from over 10 years experience, which i could put into this website by having a range of portfolio projects accessable, but maybe if theyre password protected.
- Social interactions, i could do with getting a social platform linked to the site for more advertisment channel
- how it works page, which could talk more in depth about what to expect my turn around times ect.
- portfolio could do with expanding on so each could have its own individual page which would talk more in depth about each project
- including videos 
- having a portal for clients to download their work from once they have logged into the site
- about which would include more information about me and where i have worked so my journey so far
-the checkout to also include a form inwhich the client can input personal data/ simular to the form on the product_details page
- not sure if i would require the checkout service depends if i was to use this as a purchasing platform but i think for what i want to offer you dont really have set charges for, same for websites. unless you go down the route of selling templates.

## Testing

All tests have been run manually through the console in google chrome. I have also utilising the debugger; on the lines the errors are appearing in the try and break down these errors further. Along with running the code through a syntax validator to pick up errors. I found the debugger; test and debug tool to be the most efficient with breaking down problems, utilising the console/sources and printing to the terminal to test elements working.

I have also had family members testing out the website, to get feedback on the usibility and functions.

Found bugs/ errors

issue 1 - getting the database to select 3 product IDs instead of loading all from the database. gave me the error - TypeError at /
get_object_or_404() missing 1 required positional argument: 'klass' which even baffled a few tutors, so i had to revert my working file back after all the changes recommended by tutors made more errors than i started with. Working through this again i had a double case of ()() in my context file which was pushing multiple errors out

issue 2 - when removing items from the bag, nothing was happening, no errors were printing in the terminal, and nothing logging to the console.

issue 3 - Heroku created a number of bugs for me to resolve, typically due to my inexperience with using Heroku, along with using VSC as my desired platform to build in.


Mentor review - Overall positive feedback from my mentor, Jonathon he suggested 
Manual testing for css styling was done through the live preview port, in visual code.

## Device/Browser Testing

Used Chrome Dev tools to test the responsiveness of this project on multiple devices
Check browser compatibility in Firefox, Chrome, and Safari

## Outstanding Issues

From testers feedback i also have the suggestion of adding a pop up element with a notifications. 

Also account access issues form the home page, you cannot select the dropdown, aldo mobile doesnt work either on the hamburger menu 

## Database Structure

Database structure these can be accessed in my github project.


## Deployment

The site is hosted using Heroku, any additional or new commits will automatically be updated as this links to my master branch.
Deploy to Heroku

Detailed instructions for deploying to Heroku can be found [here](https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true)


## Local Deployment

To create a local copy of this repository, follow these steps:

Go to my repo
Click the "Clone or Download" button on the top-right of the page
Click the copy icon to copy the HTTPS link
Open terminal
Change the current directory to the location where the cloned directory will be made
Type git clone <cloned URL> with the cloned URL being the URL you copied in step 3 and run the command
For more information check out GitHub's guide to cloning a repo here.


## Acknowledgement
Free imagery resource [pixabay](https://pixabay.com/)

 Debugging Article for [Javascipt] (https://dzone.com/articles/debug-javascript-using-chrome-developer-tools)

 Cross Site Request Forgery protection and how to use it [csrf] (https://docs.djangoproject.com/en/3.1/ref/csrf/#setting-the-token-on-the-ajax-request)

  This was use to help get rid of the DS.store which kept cropping up [DS.Store] (https://code.likeagirl.io/how-to-get-rid-of-ds-store-and-node-modules-in-git-repositories-d37b8a391247)


