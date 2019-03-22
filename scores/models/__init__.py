from scores.models import game
from scores.models import person
from scores.models import structure
from scores.models import team
from scores.models import venue

from scores.models.game import (FriendlyGame, Game, GroupGame, KnockoutGame,
                                LeagueGame,)
from scores.models.person import (Manager, Person, Player, Position, Referee,)
from scores.models.structure import (Competition, Country, Season,)
from scores.models.team import (Team, TeamHistory,)
from scores.models.venue import (Venue, VenueHistory,)

__all__ = ['Competition', 'Country', 'FriendlyGame', 'Game', 'GroupGame',
           'KnockoutGame', 'LeagueGame', 'Manager', 'Person', 'Player',
           'Position', 'Referee', 'Season', 'Team', 'TeamHistory', 'Venue',
           'VenueHistory', 'game', 'person', 'structure', 'team', 'venue']

