# gaiaedr3_g_rp_synthetic
This function calculates synthetic (or "deblended") G-RP for datasets from *Gaia* (e)DR3 using BP-RP photometry as input observable.
The details of this method are described in [Golovin et al. 2023, A&A, 670, A19](https://www.aanda.org/articles/aa/full_html/2023/02/aa44250-22/aa44250-22.html).

### Installation

You can install `gaiaedr3_g_rp_synthetic` directly from GitHub using `pip`. It is recommended to install this within a Python virtual environment.

```bash
pip install git+[https://github.com/AlexGolovin/gaiaedr3_g_rp_synthetic](https://github.com/AlexGolovin/gaiaedr3_g_rp_synthetic)
```

### Input
BP-RP value (or an array of values).

### Applicability range: 
0.0 mag < BP-RP < 4.25 mag

Please be reminded that the initial purpose of this tool was to be applied on the sample of nearby stars  (*d* ≤ 25 pc) from *Gaia* eDR3. No correction for reddening is necessary at this distance limit.
These corrections are to be applied at the discretion of the user, when deriving synthetic G-RP colour values for more distant objects from *Gaia* eDR3 catalogue.



### Acknowledgement:

if your paper uses results obtained with this code, please cite [Golovin et al. 2023, A&A, 670, A19](https://www.aanda.org/articles/aa/full_html/2023/02/aa44250-22/aa44250-22.html).

If you have any questions and/or comments, please contact me at `agolovin (@) lsw (dot) uni-heidelberg (dot) de`.

### A short appetizer / illustrative example:

Before | After
------------ | -------------
![](/plots/20mas_blended_HRD_o_c_colourcoded_s.png) | ![](/plots/20mas_deblended_HRD_o_c_colourcoded_s.png)


