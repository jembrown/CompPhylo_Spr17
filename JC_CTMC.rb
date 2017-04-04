######################
# Preliminaries #
######################

# Read in sequence data for both genes
data = readDiscreteCharacterData("primates.nex")

# Get some useful variables from the data. We need these later on.
n_species <- data.ntaxa()
n_branches <- 2 * n_species - 3
taxa <- data.taxa()

# Initialize indices for moves and monitors
mvi = 0 
mni = 0


######################
# Substitution Model #
######################

# create a constant variable for the rate matrix
Q <- fnJC(4) 


##############
# Tree model #
##############

out_group = clade("Galeopterus_variegatus")
# Prior distribution on the tree topology	
topology ~ dnUniformTopology(taxa, outgroup=out_group)
moves[++mvi] = mvNNI(topology, weight=5.0)
moves[++mvi] = mvSPR(topology, weight=1.0)

# Branch length prior
for (i in 1:n_branches) {
    bl[i] ~ dnExponential(10.0)
	moves[++mvi] = mvScale(bl[i])
}

TL := sum(bl)
	
psi := treeAssembly(topology, bl)


###################
# PhyloCTMC Model #
###################

# the sequence evolution model
seq ~ dnPhyloCTMC(tree=psi, Q=Q, type="DNA")

# attach the data
seq.clamp(data)


############
# Analysis #
############

mymodel = model(psi)

# add monitors
monitors[++mni] = mnScreen(TL, printgen=1000)
monitors[++mni] = mnFile(psi, filename="output/primates_cytb_JC.trees", printgen=10)
monitors[++mni] = mnModel(filename="output/primates_cytb_JC.log",printgen=10)

# run the analysis
mymcmc = mcmc(mymodel, moves, monitors, nruns=2)
mymcmc.burnin(10000,200)
mymcmc.run(30000)


###################
# Post processing #
###################

# Now, we will analyze the tree output.
# Let us start by reading in the tree trace
treetrace = readTreeTrace("output/primates_cytb_JC.trees", treetype="non-clock")
# and get the summary of the tree trace
treetrace.summarize()

map_tree = mapTree(treetrace,"output/primates_cytb_JC_MAP.tree")
con_tree = consensusTree(treetrace,"output/primates_cytb_JC_MAP.tree")

# you may want to quit RevBayes now
q()
