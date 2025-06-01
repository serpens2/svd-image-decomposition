In this project we apply custom SVD-decomposition algorithm to gray and color images.
## What is SVD?
Any $`n \times m`$ matrix $`A`$ can be written as $`A = U \Sigma V^T`$, where
- $`\Sigma`$ has the same size as $`A`$, $`V`$ is $`m \times m`$ and $`U`$ is $`n \times n`$;
- $`\Sigma`$ is a diagonal matrix with real non-negative entries $`\sigma_i`$ referred to as singular values of $`A`$;
- $`U`$ and $`V`$ are orthogonal (and real when $`A`$ is real);
- Diagonal elements of $`\Sigma`$ are sorted in descending order (convention).

The proof can be found in any linear algebra book, e.g. [[1]](#1). We denote column vectors of $`U`$ and $`V`$ as $`u_i`$
and $`v_i`$ respectively. It can be shown [[2]](#2) that this decomposition is equivalent to $`A = \sum_{i=1}^{\text{min}(n,m)} \sigma_i u_i v_i^T`$,
which is the form we use here. 

If we interpret components $`u_i v_i^T`$ corresponding to higher singular values $`\sigma_i`$ as essential parts of the matrix $`A`$, and 
components corresponding to low singular values as noise, we can construct approximation $`A_k \approx A`$ by leaving the first $`k`$ terms
in the sum.

In particular, this principle can be used in image compression, although we won't discuss it here.
## Results
We performed SVD-approximation to the following 1920 x 1200 gray image with around 1500 singular values.

![](gray_snakes.jpg)

Here's approximation with only $`k=15`$ SVs:

![](/decomposed_images/gray_snakes_k=15.jpg)

With $`k=78`$:

![](/decomposed_images/gray_snakes_k=78.jpg)

At $`k=780`$, which is around 50% of the total number of SVs, the difference is barely noticable:

![](/decomposed_images/gray_snakes_k=780.jpg)

We've also considered the following 642 x 360 color image with around 500 SVs:

![](color_snake.jpg)

We decompose it into red, green and blue channels, perform SVD on each of them, and put the resulting approximations back.

Approximation with $`k=124`$ SVs:

![](/decomposed_images/color_snake_k=124.jpg)

and with $`k=249`$ SVs:

![](/decomposed_images/color_snake_k=249.jpg)

## References
<a id="1">[1]</a> Kalman, Dan. "A singularly valuable decomposition: the SVD of a matrix." The college mathematics journal 27.1 (1996): 2-23.

<a id="2">[2]</a> Roughgarden, Tim, and Gregory Valiant. "Cs168: The modern algorithmic toolbox lecture# 9: 
The singular value decomposition (SVD) and low-rank matrix approximations." Online], http://theory.stanford.edu/~tim/s15/l/l9.pdf  .Accessed:[29 June 2019] (2015).
