from kb_loader import load_rules
from engine import ForwardChainingEngine

KB_PATH = "kb/laptop_rules.json"

def collect_initial_facts():
    facts = []
    if input("Is your budget low? (y/n): ").lower().startswith("y"):
        facts.append("budget_low")

    if input("Is your budget medium? (y/n): ").lower().startswith("y"):
        facts.append("budget_medium")

    if input("Is your budget high? (y/n): ").lower().startswith("y"):
        facts.append("budget_high")

    if input("Is portability important? (y/n): ").lower().startswith("y"):
        facts.append("portable")

    if input("Do you need long battery life? (y/n): ").lower().startswith("y"):
        facts.append("long_battery")
    
    if input("Are you wanting it to run games? (y/n): ").lower().startswith("y"):
        facts.append("gaming")
    
    if input("Do you do creative work? (y/n): ").lower().startswith("y"):
        facts.append("creative_work")
    
    if input("Will you mainly do office / school work? (y/n): ").lower().startswith("y"):
        facts.append("office_only")
    
    if input("Prefer Windows? (y/n): ").lower().startswith("y"):
        facts.append("pref_os_windows")

    if input("Prefer macOS? (y/n): ").lower().startswith("y"):
        facts.append("pref_os_macos")

    if input("Prefer Linux? (y/n): ").lower().startswith("y"):
        facts.append("pref_os_linux")

    if input("Do you need AI acceleration? (y/n): ").lower().startswith("y"):
        facts.append("needs_ai_accel")

    if input("Do you need a large screen? (y/n): ").lower().startswith("y"):
        facts.append("large_screen")

    if input("Do you travel often? (y/n): ").lower().startswith("y"):
        facts.append("travel_often")

    return facts

def main():
    # Loading Rules
    rules = load_rules(KB_PATH)

    # Creating the engine
    engine = ForwardChainingEngine(rules)

    # Collect user facts
    initial_facts = collect_initial_facts()
    engine.assert_facts(initial_facts)

    # Run chaining
    engine.run()

    # Retrieve results
    results = engine.conclusions()

    # Print recommendations
    print()
    print()
    for r in results["recommendations"]:
        print("> Recommendation:", r.replace("recommend:", ""))

    # Print specs
    print()
    if results["specs"]:
        for s in results["specs"]:
            print("> Specs:", s.replace("spec:", ""))

    # Print Reasoning
    print()
    for step in engine.trace:
        print(f"> Explanation: derived from rule '{step['rule']}'")

if __name__ == "__main__":
    main()
