from pyrokinetics import Pyro, template_dir

# Equilibrium file
eq_file = template_dir / "test.geqdsk"

# Kinetics data file
kinetics_file = template_dir / "jetto.cdf"

# Load up pyro object
pyro = Pyro(
    eq_file=eq_file,
    eq_type="GEQDSK",
    kinetics_file=kinetics_file,
    kinetics_type="JETTO",
)

# Generate local parameters at psi_n=0.5
pyro.load_local(psi_n=0.5, local_geometry="Miller")

# Change GK code to GS2
pyro.gk_code = "GS2"

# Write single input file using my own template
pyro.write_gk_file(file_name="test_jetto.gs2", template_file="step.in")

# Select code as CGYRO
pyro.gk_code = "CGYRO"

# Write CGYRO input file using default template
pyro.write_gk_file(file_name="test_jetto.cgyro")
