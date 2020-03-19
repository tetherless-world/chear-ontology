# Setup
If you are doing this for the first time, you need to install the software correctly:

```
virtualenv -p `python3` --no-site-packages venv/
source venv/bin/activate
pip install -r requirements.txt
```

If you're coming back to rebuild, be sure to activate the virtual environment again:

```
source venv/bin/activate
```

# CHEAR Ontology

To build the ontology:

```
invoke build
```

# HHEAR Ontology

To build the HHEAR ontology:

```
invoke buildhhear
```

# Converting XLSX files to HHEAR

To convert an XLSX file (like SDDs or SSDs) from CHEAR to HHEAR, run the following command:

```
invoke chear2hhear -i <inputfile> -o <outputfile>
```
