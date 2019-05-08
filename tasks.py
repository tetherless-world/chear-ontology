from invoke import task, run

#from fabric.api import local, lcd, get, env
#from fabric.operations import require, prompt
#from fabric.utils import abort
import requests
import rdflib
import getpass
import os.path
import os
import setlr
from os import listdir
from rdflib import *

import logging

CHEAR_DIR='chear.d/'
SETL_FILE='ontology.setl.ttl'

ontology_setl = Namespace('https://hadatac.org/setl/')
setl = Namespace('http://purl.org/twc/vocab/setl/')
prov = Namespace('http://www.w3.org/ns/prov#')
dc = Namespace('http://purl.org/dc/terms/')
pv = Namespace('http://purl.org/net/provenance/ns#')

logging_level = logging.INFO
logging.basicConfig(level=logging_level)

@task
def build(ctx):
    setl_graph = Graph()
    setl_graph.parse(SETL_FILE,format="turtle")
    cwd = os.getcwd()
    formats = ['ttl','owl','json']
    ontology_output_files = [setl_graph.resource(URIRef('file://'+cwd+'/chear.'+x)) for x in formats]
    print (len(setl_graph))
    for filename in os.listdir(CHEAR_DIR):
        if not filename.endswith('.ttl') or filename.startswith('#'):
            continue
        print('Adding fragment', filename)

        fragment = setl_graph.resource(BNode())
        for ontology_output_file in ontology_output_files:
            print(ontology_output_file.identifier, list(ontology_output_file[prov.wasGeneratedBy]))
            ontology_output_file.value(prov.wasGeneratedBy).add(prov.used, fragment)
        fragment.add(RDF.type, setlr.void.Dataset)
        fragment_extract = setl_graph.resource(BNode())
        fragment.add(prov.wasGeneratedBy, fragment_extract)
        fragment_extract.add(RDF.type, setl.Extract)
        fragment_extract.add(prov.used, URIRef('file://'+CHEAR_DIR+filename))

    setlr._setl(setl_graph)

