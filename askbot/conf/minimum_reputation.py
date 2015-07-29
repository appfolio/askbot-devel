"""
Settings for minimum reputation required for
a variety of actions on the askbot askbot
"""
from askbot.conf.settings_wrapper import settings
from askbot.conf.super_groups import REP_AND_BADGES
from askbot.deps import livesettings
from django.utils.translation import ugettext_lazy as _

MIN_REP = livesettings.ConfigurationGroup(
    'MIN_REP',
    _('Karma thresholds'),
    ordering=0,
    super_group = REP_AND_BADGES
)

settings.register(
    livesettings.IntegerValue(
        MIN_REP,
        'MIN_REP_TO_AUTOAPPROVE_USER',
        default=1,
        description=_('Become approved'),
        help_text=_('Approved users bypass moderation and skip recaptcha')
    )
)

settings.register(
    livesettings.IntegerValue(
        MIN_REP,
        'MIN_REP_TO_VOTE_UP',
        default=1,
        description=_('Upvote')
    )
)

settings.register(
    livesettings.IntegerValue(
        MIN_REP,
        'MIN_REP_TO_VOTE_DOWN',
        default=1,
        description=_('Downvote')
    )
)

settings.register(
    livesettings.IntegerValue(
        MIN_REP,
        'MIN_REP_TO_ANSWER_OWN_QUESTION',
        default=1,
        description=_('Answer own question immediately')
    )
)

settings.register(
    livesettings.IntegerValue(
        MIN_REP,
        'MIN_REP_TO_ACCEPT_OWN_ANSWER',
        default=1,
        description=_('Accept own answer')
    )
)

settings.register(
    livesettings.IntegerValue(
        MIN_REP,
        'MIN_REP_TO_ACCEPT_ANY_ANSWER',
        default=1,
        description=_('Accept any answer')
    )
)

settings.register(
    livesettings.IntegerValue(
        MIN_REP,
        'MIN_REP_TO_FLAG_OFFENSIVE',
        default=1,
        description=_('Flag offensive')
    )
)

"""
#this is disabled to possibly be completely removed later
settings.register(
    livesettings.IntegerValue(
        MIN_REP,
        'MIN_REP_TO_LEAVE_COMMENTS',
        default=1,
        description=_('Leave comments')
    )
)
"""

settings.register(
    livesettings.IntegerValue(
        MIN_REP,
        'MIN_REP_TO_DELETE_OTHERS_COMMENTS',
        default=100000,
        description=_('Delete comments posted by others')
    )
)

settings.register(
    livesettings.IntegerValue(
        MIN_REP,
        'MIN_REP_TO_DELETE_OTHERS_POSTS',
        default=100000,
        description=_('Delete questions and answers posted by others')
    )
)

settings.register(
    livesettings.IntegerValue(
        MIN_REP,
        'MIN_REP_TO_DELETE_OWN_QUESTIONS',
        default=1,
        description=_('Delete own questions')
    )
)

settings.register(
    livesettings.IntegerValue(
        MIN_REP,
        'MIN_REP_TO_UPLOAD_FILES',
        default=1,
        description=_('Upload files')
    )
)

settings.register(
    livesettings.IntegerValue(
        MIN_REP,
        'MIN_REP_TO_INSERT_LINK',
        default=1,
        description=_('Insert clickable links')
    )
)

settings.register(
    livesettings.IntegerValue(
        MIN_REP,
        'MIN_REP_TO_SUGGEST_LINK',
        default=1,
        description=_('Insert link suggestions as plain text'),
        help_text=_(
            'This value should be smaller than that for "insert clickable links". '
            'This setting should stop link-spamming by newly registered users.'
        )
    )
)

settings.register(
    livesettings.IntegerValue(
        MIN_REP,
        'MIN_REP_TO_RETAG_OTHERS_QUESTIONS',
        default=1,
        description=_('Retag questions posted by other people')
    )
)

settings.register(
            livesettings.IntegerValue(
        MIN_REP,
        'MIN_REP_TO_EDIT_WIKI',
        default=1,
        description=_('Edit community wiki posts')
    )
)

settings.register(
    livesettings.IntegerValue(
        MIN_REP,
        'MIN_REP_TO_EDIT_OTHERS_POSTS',
        default=1,
        description=_('Edit posts authored by other people')
    )
)

settings.register(
    livesettings.IntegerValue(
        MIN_REP,
        'MIN_REP_TO_VIEW_OFFENSIVE_FLAGS',
        default=1,
        description=_('View offensive flags')
    )
)

settings.register(
    livesettings.IntegerValue(
        MIN_REP,
        'MIN_REP_TO_CLOSE_OTHERS_QUESTIONS',
        default=100000,
        description=_('Close and reopen questions')
    )
)

settings.register(
    livesettings.IntegerValue(
        MIN_REP,
        'MIN_REP_TO_HAVE_STRONG_URL',
        default=1,
        description=_('Remove rel=nofollow from own homepage'),
        help_text=_(
                    'When a search engine crawler will see a rel=nofollow '
                    'attribute on a link - the link will not count towards '
                    'the rank of the users personal site.'
                   )
    )
)

settings.register(
    livesettings.IntegerValue(
        MIN_REP,
        'MIN_REP_TO_POST_BY_EMAIL',
        default=1,
        description=_('Make posts by email')
    )
)

settings.register(
    livesettings.IntegerValue(
        MIN_REP,
        'MIN_REP_TO_TRIGGER_EMAIL',
        default=1,
        description=_('Trigger email notifications'),
        help_text=_('Reduces spam')
    )
)

settings.register(
    livesettings.IntegerValue(
        MIN_REP,
        'MIN_REP_TO_TWEET_ON_OTHERS_ACCOUNTS',
        default=100000,
        description=_('Trigger tweets on others accounts'),
        help_text=_('Reduces spam')
    )
)
