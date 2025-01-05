

# ############### tuples ###################################
##############################################################
# 1. tuples are similr to list except immutable (like string)

# init
t = tuple()
t2 = ()

# singleton tuple exception
t3 = (1, )

# Sc: Where we want a var to be only read-only
# Example => keys of a dict


# Iterating over tuples ( Exactly same as lists, just copy-pasted )
tu = (1, 2, 3, 4, 5, 6)

# way 1, printing only values
for te in tu:
    print(te)
print()

# way 2, printing both idx and values
for idx, te in enumerate(tu):
    print(idx, te)
print()

# way3, printing USING idx
for idx in range(len(tu)):
    print( idx, tu[idx] )
print()

##############################################################
##############################################################




# ############### dict ###################################
##############################################################
# 1. dicts => { "key" : value }

# init
d = dict()
d2 = {}

# example
d3 = {'1': "Prateek", '2': "Little"}


# BTS
# This is implemented as a hash-table 
# Operations complexity: O(1) Amortized
# But, in WC: O(n), due to collisions


# NOTE:- Sc: When domain of keys are [0, 1, 2, 3, ...., n-1] => Better to use list
# Where idx of lists can be implicitly though of as keys (Don't use dicts)


# Iterating over a dict
for key, value in d3.items():
    print(key, value)


# What's the type of keys of a dict?
print( d3.keys() ) # Idea is tuplelike-type

##############################################################
##############################################################
