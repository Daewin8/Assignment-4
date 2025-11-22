from kb_loader import load_rules
from engine import ForwardChainingEngine

def run_inference_with_facts(facts):
    rules = load_rules("kb/laptop_rules.json")
    engine = ForwardChainingEngine(rules)
    for f in facts:
        engine.assert_fact(f)
    engine.run()
    return engine.facts

def test_premium_ultrabook():
    input_facts = ["budget_high", "portable", "long_battery"]
    results = run_inference_with_facts(input_facts)
    assert "recommend:premium_ultrabook" in results

def test_budget_student_laptop():
    input_facts = ["budget_low", "portable"]
    results = run_inference_with_facts(input_facts)
    assert "recommend:budget_student_laptop" in results

def test_gaming_laptop():
    input_facts = ["budget_high", "needs_gpu"]
    results = run_inference_with_facts(input_facts)
    assert "recommend:gaming_laptop" in results
