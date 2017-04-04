# Define our data
data <- 30

# Set the prior on the binomial probability
# A "skeptical" Beta distribution
p ~ dnBeta(0.1,0.1)

# Set up moves on p
moves[1] = mvSlide(p)

# Define our model and clamp our data
y ~ dnBinomial(p,50)
y.clamp(data)

# Create the model
binModel = model(p)

# Create monitors to see what's happening
monitors[1] = mnScreen(printgen=1,p)
monitors[2] = mnModel(filename="../binMCMC_output.log",printgen=1)

# Create MCMC object
binMCMC = mcmc(binModel,monitors,moves)

# Run the MCMC!
binMCMC.run(generations=100000)
