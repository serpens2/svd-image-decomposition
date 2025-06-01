import numpy as np
'''
Returns SVD of a real matrix A in the form:
- vals: array of non-zero singular values (with precision given by trunc_val)
- u_vecs: array of left singular vectors
- vecs: array of right singular vectors (not transposed!)

This gives decomposition of A into sum of the expression
vals[i] * np.outer(u_vecs[i],vecs[i])
over i
'''
def SVD(A, trunc_val=1e-6):
    vals,vecs = np.linalg.eig( A.T @ A )
    # Singular values/vectors must be real, so any complex component is
    # a numerical error
    vals = np.real(vals) 
    vecs = np.real(vecs)
    # Similarly, singular values must be non-negative. We can also
    # discard zeros
    vals[ vals < 0 ] = 0
    vals = np.sqrt(vals)
    vals = vals[ vals >= trunc_val ]
    # Sorting singular values in descending order, and applying the same
    # sort to right singular vectors
    ncols = np.argsort(vals)[::-1]
    vals = vals[ncols]    
    vecs = vecs[:,ncols].T
    # Computing left singular vectors (note that vals[i] != 0)
    u_vecs = np.array([ (A @ vecs[i].T)/vals[i] for i in range(len(vals)) ])
    return u_vecs, vals, vecs
###
'''
Example with random n x m matrix A. You can change dimensions
to check cases when n = m, n < m or n > m
'''
if __name__ == '__main__':
    A = np.random.rand(5,3)
    print('---A---')
    print(A)
    U, Sigma, V = SVD(A)
    print('---')
    print('Singular values:')
    print(Sigma)
    A_reconst = np.zeros_like(A).astype('float')
    for i in range(len(Sigma)):
        A_reconst += Sigma[i] * np.outer( U[i], V[i] ) 
    print('---A_reconst---')
    print(A_reconst)
        
