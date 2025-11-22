from dataclasses import dataclass
from typing import List, Set, Dict, Any

@dataclass
class Rule:
    antecedents: List[str]
    consequent: str
    priority: int = 0
    name: str = ""

class ForwardChainingEngine:
    def __init__(self, rules: List[Rule]):
        self.rules = rules
        self.facts: Set[str] = set()
        self.trace: List[Dict[str, Any]] = []

    def assert_facts(self, initial: List[str]) -> None:
        """Store initial facts into the working memory."""
        self.facts.update(initial)

    def can_fire(self, rule: Rule) -> bool:
        """
        A rule can fire when:
        - All antecedents are already true in fact set.
        - The consequent is NOT already in fact set (avoid loops).
        """
        # All antecedents must be present
        for ant in rule.antecedents:
            if ant not in self.facts:
                return False

        # Consequent must be new
        return rule.consequent not in self.facts

    def run(self) -> None:
        """
        Main forward-chaining loop:
        - Loop until no rule fires.
        - Each iteration: find rules that can fire,
          pick one (simple priority + name sorting),
          apply it, record the trace.
        """
        fired = True
        while fired:
            # collect rules that can fire
            possible = [r for r in self.rules if self.can_fire(r)]

            if not possible:
                fired = False
                break

            # Choosing a rule and firing it
            possible.sort(key=lambda r: (r.priority, r.name))
            chosen = possible[0]
            self.facts.add(chosen.consequent)

            # Save for the explanation
            self.trace.append({
                "rule": chosen.name,
                "consequent": chosen.consequent,
                "from": chosen.antecedents
            })

    def conclusions(self) -> Dict[str, List[str]]:
        """
        Separate outcomes into:
        - recommendations (recommend:...)
        - specs (spec:...)
        - raw other facts
        """
        recommendations = []
        specs = []
        others = []

        for f in self.facts:
            if f.startswith("recommend:"):
                recommendations.append(f)
            elif f.startswith("spec:"):
                specs.append(f)
            else:
                others.append(f)

        return {
            "recommendations": sorted(recommendations),
            "specs": sorted(specs),
            "other": sorted(others)
        }