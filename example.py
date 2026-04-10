import numpy as np
import matplotlib.pyplot as plt
from astropy.table import Table
from g_rp_synth_deblending import g_rp_synth

def run_example():
    print("--- Gaia Synthetic G-RP Example ---")
    
    # 1. Generate some mock Gaia data spanning the applicability range (and a bit outside)
    print("Generating mock BP-RP data...")
    mock_bp_rp = np.linspace(-0.5, 4.5, 500)
    
    # Create a mock Astropy Table to simulate a typical user's workflow
    input_table = Table()
    input_table['bp_rp'] = mock_bp_rp
    
    # Add mock flux errors (simulating mostly good data, with a few bad ones)
    input_table['phot_bp_mean_flux_over_error'] = np.random.uniform(15, 100, 500)
    input_table['phot_rp_mean_flux_over_error'] = np.random.uniform(15, 100, 500)
    
    # 2. Filter for quality based on SNR > 20 in both BP and RP
    print("Filtering data for S/N > 20...")
    mask = (input_table['phot_bp_mean_flux_over_error'] > 20) & \
           (input_table['phot_rp_mean_flux_over_error'] > 20)
    
    valid_sources = input_table[mask]
    bp_rp_colors = np.array(valid_sources['bp_rp'])
    
    # 3. Call the deblending function
    print("Calculating synthetic G-RP...")
    synthetic_g_rp = g_rp_synth(bp_rp_colors)
    
    # 4. Attach the results back to the table
    valid_sources['synthetic_g_rp'] = synthetic_g_rp
    print(f"Successfully processed {len(valid_sources)} valid sources.")
    
    # 5. Plot the results to visually verify the spline
    print("Plotting results...")
    plt.figure(figsize=(6, 5))
    plt.scatter(valid_sources['bp_rp'], valid_sources['synthetic_g_rp'], 
                s=5, color='teal', label='Synthetic G-RP')
    
    # Formatting the plot
    plt.rcParams['text.usetex'] = True
    plt.title(r'Output vs. input in \texttt{gaiaedr3-g-rp-synthetic}', fontsize=14)
    plt.xlabel('Input: BP-RP [mag]')
    plt.ylabel('Output: Synthetic G-RP [mag]')
    plt.axvspan(0.0, 4.25, color='gray', alpha=0.1, label='Applicability Range')
    plt.grid(True, linestyle='--', alpha=0.4)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_example()
