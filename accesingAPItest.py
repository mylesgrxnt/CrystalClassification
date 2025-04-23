from mp_api.client import MPRester
from secretInfo import APIKEY

with MPRester(APIKEY) as mpr:
  docs = mpr.materials.summary.search(
    material_ids=["mp-149", "mp-13", "mp-22526"]
  )
  example_doc = docs[2]
  mpid = example_doc.material_id
  formula = example_doc.formula_pretty
  print(formula)