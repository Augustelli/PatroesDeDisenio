from observer import Publisher, Subscriber

pub = Publisher()

sub1 = Subscriber("Subscriber 1")
sub2 = Subscriber("Subscriber 2")

pub.add_subscriber(sub1)
pub.add_subscriber(sub2)

pub.notify_subscribers("Hello, subscribers!")

pub.remove_subscriber(sub1)

pub.notify_subscribers("Another message")