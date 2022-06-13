# gaiaedr3_g_rp_synthetic
This function calculates synthetic (or "deblended") G-RP for datasets from *Gaia* eDR3 using BP-RP photometry as input observable.
The details of this method are described in [Golovin et al. 2022, A&A, submitted]().

### Input
BP-RP value (or an array of values). Note! BP-RP array needs to be in strictly increasing order.

### Applicability range: 
0.0 < BP-RP < 4.25

Please be reminded that the initial purpose of this tool was to be applied on the sample of nearby stars  (*d* ≤ 25 pc) from *Gaia* eDR3. No correction for reddening is necessary at this distance limit.
These corrections are to be applied at the discretion of the user, when deriving synthetic G-RP colour values for more distant objects from *Gaia* eDR3 catalogue.



### Acknowledgement:

if your paper uses results obtained with this code, please cite [Golovin et al. 2022, A&A, submitted]().

If you have any questions and/or comments, please contact me at `agolovin (@) lsw (dot) uni-heidelberg (dot) de`.

### A short appetizer with a few illustrative examples:

Before | After
------------ | -------------
![](/plots/20mas_blended_HRD_o_c_colourcoded_s.png) | ![](/plots/20mas_deblended_HRD_o_c_colourcoded_s.png)


