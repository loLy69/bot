"""
Data models for the Purchase Planning Assistant
"""
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class PurchasePlan:
    """A single purchase plan entry"""
    id: int
    user_id: int
    title: str
    category: str
    estimated_price: int
    created_at: datetime = field(default_factory=datetime.now)

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'user_id': self.user_id,
            'title': self.title,
            'category': self.category,
            'estimated_price': self.estimated_price,
            'created_at': self.created_at.isoformat() if isinstance(self.created_at, datetime) else self.created_at,
        }


CATEGORIES = [
    'clothing',
    'tech',
    'home',
    'travel',
    'entertainment',
    'other',
]

CATEGORY_ICONS = {
    'clothing': '👕',
    'tech': '📱',
    'home': '🏠',
    'travel': '✈️',
    'entertainment': '🎮',
    'other': '📌',
}

CATEGORY_LABELS = {
    'clothing': 'Одежда',
    'tech': 'Техника',
    'home': 'Быт',
    'travel': 'Поездки',
    'entertainment': 'Развлечения',
    'other': 'Другое',
}

CATEGORY_LABELS_RU = {
    'Одежда': 'clothing',
    'Техника': 'tech',
    'Быт': 'home',
    'Поездки': 'travel',
    'Развлечения': 'entertainment',
    'Другое': 'other',
}
