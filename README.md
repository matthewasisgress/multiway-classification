# multiway-classification
Application of the R package **cpfa** to the MNIST dataset. A brief 
demonstration of multiway classification with real data.

Author: Matthew Asisgress

## License

This project is dual-licensed. All R code, including the `mcrd.Rmd` source file, 
is licensed under the MIT license. See the `LICENSE` file for details. The 
generated report (`mcrd.pdf`), as a derivative work of the MNIST dataset, is 
licensed under the Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0) 
license.

## R packages

This project uses the R programming language (R Core Team, 2025). In addition, 
this project uses two R packages found on The Comprehensive R Archive Network 
(i.e., CRAN) including: **cpfa** (Asisgress, 2025) and **dslabs** 
(Irizarry and Gill, 2025). Note that the R package **cpfa** depends
upon the R package **mulitway** (Helwig, 2025), which itself depends on the R 
package **CMLS** (Helwig, 2025).

## Data

This application uses the MNIST dataset (LeCun, Cortes, and Burges, 1998; LeCun 
et al., 2002), which is automatically downloaded when the R Markdown file is 
run. Yann LeCun and Corinna Cortes hold the copyright of the MNIST dataset, 
which is a derivative work from original NIST datasets. The MNIST dataset is 
made available under the terms of the CC BY-SA 3.0 license, which can be viewed 
here: <https://creativecommons.org/licenses/by-sa/3.0/deed.en>.

## References

Asisgress, M. (2025). cpfa: Classification with Parallel Factor Analysis. 
R package version 1.2-2, <https://CRAN.R-project.org/package=cpfa>.

Helwig, N. (2025). CMLS: Constrained Multivariate Least Squares.
R package version 1.1, <https://CRAN.R-project.org/package=CMLS>.

Helwig, N. (2025). multiway: Component Models for Multi-Way Data. 
R package version 1.0-7, <https://CRAN.R-project.org/package=multiway>.

Irizarry, R., Gill, A. (2025). dslabs: Data Science Labs.
R package version 0.9.0, <https://CRAN.R-project.org/package=dslabs>.

LeCun, Y., Bottou, L., Bengio, Y., and Haffner, P. (2002). Gradient-based 
learning applied to document recognition. Proceedings of the IEEE, 86(11), 
2278–2324. <https://doi.org/10.1109/5.726791>.

LeCun, Y., Cortes, C., and Burges, C. (1998). The MNIST database of handwritten 
digits. <http://yann.lecun.com/exdb/mnist/>.

R Core Team (2025). R: A Language and Environment for Statistical Computing. R 
Foundation for Statistical Computing, Vienna, Austria. 
<https://www.R-project.org/>.