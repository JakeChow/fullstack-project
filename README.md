# Intro

# Welcome to the Sure Associate Software Engineer take-home! We've loved getting to know you as a person and now we are excited to see how you approach some software problems!

# Purpose

# The purpose of this interview is to assess basic technical knowledge, see how you write and organize your code, and understand where you are in your software career. We won't be judging you on using the most complicated tech or coming up with contrived problems you can solve to show off. We just want to see how well you can read instructions and create high quality code!

# Getting started

1. Fork the project on your github
2. Create a branch with a relevant name containing both FE and BE work
3. Upon completion, please create a PR from that branch with all of your changes
4. Submit a link to that PR to the recruiting team for engineering review

# Instructions

# Frontend

# For the frontend we would like you to make a simple form. Everything about that is up to you. You should use the `intsureview_fe` folder as a starting point. The goal is for a clean user interface and experience that gets the job done. We aren't looking for incredible designs or multiple user flows. A basic form that you can submit and handles a response will suffice.

## Page Layout

1. Create a header component with the name of a fake company of your choice.
2. Create a central content component that will hold all of the form components.
3. Create a footer containing something you'd expect to find in the footer.

## Form Content

1. Create a text input.
2. Create a select input that handles the values `Yes` and `No`.
3. Create 3 more inputs of your choice.
4. Validate the content of at least one field on this form.

## Functionality

1. Create a submit button that, when clicked, sends your form data to the backend.
2. Handle the backend response on the frontend however you see fit!

# Backend

# For the backend we would like you to make a simple API endpoint that handles your form submission, and sends back a response for the frontend to use. We have provided a simple Django project `intsureview_be`. The goal here is for you to create an endpoint that handles the user input and sends a response back to the frontend.

## API Functionality

1. There should be at least one route on the backend for the FE to hit with its form data.
2. There should be distinct responses for success/failure of the endpoint call.
3. There should be a restricted set of HTTP request methods the endpoint allows (GET, PUT, POST, etc.)

## Tips

1. Read the instructions top to bottom before getting to work. Make sure you are thinking about the whole set of requirements at once, not just one at a time.
2. Format your code. At a minimum, use your editor's built-in formatting. Readability is key!
3. Write relevant comments. Did you take a shortcut or make a workaround that may be atypical? That's ok! Just drop a comment. An important part of writing software is knowing how and when to take a shortcut and communicating that to your team.
4. Use whatever additional 3rd party libraries you want! It is unlikely any of us can rewrite a more effective sorting algorithm in one hour than what is built in to our language of choice! That isn't the point anyway. Focus on getting everything done well while using the tools and resources available to you!
5. Don't overdo it! This was designed to be respectful of everyones time and ensure an inclusive interview process. It is ok if it takes more or less time, but please don't feel like you must use the entire three days on this project!
6. Have a little fun with it! We left the exact requirements open ended but provided concrete base requirements. If you want to run an icecreamtech and collect flavor preferences, or an insuretech and collect personal info, all are welcome! Just make sure to include the required input types and follow the instructions.
