#!/usr/bin/env python3

"""
Assignment 3 Outline

Markov Chain Monte Carlo

Due: Wednesday, 2.22.17

You can turn in either raw Python code (like this file) or a Jupyter notebook.

Remember to include LOTS of comments, including docstrings for functions. Be
sure to include specific notes about the types of distributions you're using
to calculate probabilities or draw random numbers. Remember, someone else
generally familiar with MCMC should be able to read this and very quickly
understand what you're doing and how.
"""

# Import necessary libraries, classes, and modules. Remember that you'll need
# to calculate some PMFs and PDFs, draw random numbers, and do some plotting.



# Define some data. Start with the binomial and then try a normal (Gaussian).

                                                                  

# Define a function to calculate a likelihood. Name it something generic (e.g.,
# like()), so that you can change your model later on and the code will still 
# run. Also, include a boolean switch to have this function always return 1, 
# in order to test the prior.



# Define a function to calculate a prior probability (mass or density). Again, 
# use a generic name (e.g., prior()).

                     
                     
# Define a function to calculate the unnormalized posterior density (i.e., 
# just multiply the prior and likelihood.)



# Define a function to draw a new value for the parameter(s) of interest using
# a proposal distribution. Again, be generic with the name so that you can try
# different proposal distributions using the same function.



# Define a function to accept or reject proposed moves based on the ratio of
# their posterior densities. If you use an asymmetric proposal distribution, 
# remember that you'll also need to include a Hasting's ratio.


# Create lists to store parameter values, prior probabilities, likelihoods, 
# and posterior densities.



# Define a function to run the chain! Begin by defining starting conditions for
# the Markov chain, including the number of generations it will run, the 
# starting parameter value(s), and the starting posterior density 
# (unnormalized). Use a for loop to iterate through the specified number of 
# generations. Each step will involve proposing new values, deciding whether
# to accept or reject those values, then recording the new value.
# HINT: It can be helpful to write a function that allows you to pass relevant
# information (e.g., the number of generations, the lists to store values, etc)
# as arguments. Also, it can be very cumbersome and unnecessary to record 
# _every_ parameter value that's sampled. How could you write out values every
# n-th generation?



# Create trace plots of parameter values, priors, likelihoods, and posteriors.



# Create histograms of parameter values, priors, likelihoods, and posteriors.



"""
Now use the code you've written above to explore answers to these questions. 
Ideally, the code you've written is sufficiently generic, so you can simply
call the code above with different arguments. This will make it much easier to
remember the conditions you explored. If you write this assignment in a
Jupyter notebook, you can also include the answers as comments, plots, etc.

(1) How does the size of the proposal distribution affect the efficiency of
    the chain? Try a very small distribution, a very large one, and one that 
    seems like it should be about the width of the posterior peak.
    
(2) How long does it take for the chain to "burn in"? Try this with different
    proposal distributions and datasets of different sizes.
    
(3) Define a dataset where the values could be draws from a Normal. Have the
    chain explore the joint posterior distribution for both the mean and the
    standard deviation. Remember that you'll need to include proposals that 
    change both parameter values. What happens when the starting values for one
    or both parameters are very far away from the peak of the posterior? Try
    plotting the two parameter values from each generation against each other.
    Do they seem correlated?
    
(4) How confident are you that you've sampled the posterior distribution well?
    What strategies can you use to make sure? Can you run multiple, independent
    analyses using the code you wrote above?
"""