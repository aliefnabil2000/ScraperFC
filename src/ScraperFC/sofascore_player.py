from datetime import datetime
from dataclasses import dataclass
import pandas as pd

@dataclass
class SofascorePlayer:
    id: int
    name: str
    team_name: str
    team_id: int
    position: str | None
    positions_detailed: list[str] | None
    weight: int | None
    height: int | None
    dob: datetime | None
    preferred_foot: str | None
    country: str | None
    contract_until: datetime | None
    market_value: int | None
    market_value_currency: str | None
    career_stats: pd.DataFrame

    def __repr__(self) -> str:
        return f"SofascorePlayer(id={self.id}, name={self.name})"

    @staticmethod
    def to_dataframe(players: "list[SofascorePlayer]") -> pd.DataFrame:
        """Convert a list of SofascorePlayer to a flat DataFrame (excludes career_stats)."""
        rows = []
        for p in players:
            rows.append({
                "id": p.id,
                "name": p.name,
                "team_name": p.team_name,
                "team_id": p.team_id,
                "position": p.position,
                "positions_detailed": p.positions_detailed,
                "weight": p.weight,
                "height": p.height,
                "dob": p.dob,
                "preferred_foot": p.preferred_foot,
                "country": p.country,
                "contract_until": p.contract_until,
                "market_value": p.market_value,
                "market_value_currency": p.market_value_currency,
            })
        return pd.DataFrame(rows)
