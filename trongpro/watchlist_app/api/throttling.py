from rest_framework.throttling import UserRateThrottle


class ReviewCreateThrottler(UserRateThrottle):
    scope = 'review-create'


class ReviewListThrottler(UserRateThrottle):
    scope = 'review-list'
