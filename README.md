# Personal Advertising/ Design services Project-MS4
design services and portfolio for educational purposes only, which i wish to expand upon marking completion. bootstrap styling template has been used for this project.

Fitness tracker can be accesses here:
insert heroku link here


## UX & UI
both desktop and mobile friendly, landing on the homepage you have an intro, breif overview of who i am, and the skills i could offer with 3 select services that are standard packages. The aim with this website is for further advertisement and for me to gain more freelance on completion of my course whether this be graphic design or more front end developement. 

The design is based around being clean and concise for usability, as the main focus of the site, utilising the styling template bootstrap.

### Wireframe
 my Wireframes can be viewed [here](https://xd.adobe.com/view/4744aed7-1936-4de1-827a-5927a5d2836f-1217/)


## Technologies Used

Python - used as the backend language to connect what the user sees and the data they have input
HTML5 - used to semantically structure website
CSS3 - used for styling of HTML
Javascript - used in conjunction with jQuery to create an interactive user experience
bootstrap - used for quick, responsive styling
Pixabay - used for free stock photos

## User stories

1) "Sam designs has alot of potential especially for the level of services she could offer, be great if you expand more in depth into your portfolio and what each project/ piece entailed"

2) "I typically go agency based for anything we need design or developement wise, but having someone who could turn things around faster and who could get to know our brand on a different level would be great"

## Strategy

As the target audience is broad for design and development services, I have kept the interface clean and ease of navigation. Users can quickly look through available services, or even search for what they may require, on the services page you can request a tailored quote as no job is the same when it comes to development or design, each enquiry can vary from dependent on the company. So the direction i took with the service page is for clients to complete a form in which i could check my schedule and quote appropriately for what they require.

## Structure

Responsiveness and clarity were my goal for this site. It is not feature heavy because I don't want to over complicate something that should be simple.

## Features

This project is built with Python, Django, CSS, bootstrap, and uses Django to store user data. I chose to use bootstrap to keep a nice, clean grid feel to the site.

- service blocks -  users can easily see and scroll through service which are displayed in a card block formats.

- Login - Users have the ability to create an account, which for future purposes could turn into a client portal for accessing and downloading their workable files from

- Imagery - All imagery is from my portfolio which i have permission to use from each of the brands, aslong as the products are already in the public eye.

## Future Features

My design career extends from over 10 years experience, which i could put into this website with alot more time.

- Social interactions, i could do with getting a social platform linked to the site for more advertisment channel
- how it works page, which could talk more in depth about what to expect my turn around times ect.
- portfolio could do with expanding on so each could have its own individual page which would talk more in depth about each project
- including videos 
- having a portal for clients to download their work from once they have logged into the site


## Testing

All tests have been run manually through the console in google chrome. I have also utilising the debugger; on the lines the errors are appearing in the try and break down these errors further. Along with running the code through a syntax validator to pick up errors. I found the debugger; test and debug tool to be the most efficient with breaking down problems, utilising the console/sources.

I have also had family members testing out the website, to get feedback on the usibility and functions.

Found bugs/ errors

issue 1 - getting the database to select 3 product IDs instead of loading all from the database. gave me the error - TypeError at /
get_object_or_404() missing 1 required positional argument: 'klass' which even baffled a few tutors, so i had to revert my working file back after all the changes recommended by tutors made more errors than i started with.

issue 2 - Heroku created a number of bugs for me to resolve, typically due to my inexperience with using Heroku, along with using VSC as my desired platform to build in. 



Mentor review - Overall positive feedback from my mentor, Jonathon he suggested 

Manual testing for css styling was done through the live preview port, in visual code.

## Device/Browser Testing

Used Chrome Dev tools to test the responsiveness of this project on multiple devices
Check browser compatibility in Firefox, Chrome, and Safari

## Outstanding Issues

From testers feedback i also have the suggestion of adding a pop up element with a notifications. 

## Database Structure

Database structure these can be accessed in my github project.
screenshot1.png
screenshot2.png

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


Onload Attribute isn't supported on all elements in particular it won't work on a div tag, here's a list of where it's valid to use: https://www.w3schools.com/tags/ev_onload.asp