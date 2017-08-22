import os
import flipper

def fake_old_func():
    return 'old'

def fake_new_func():
    return 'new'

def test_flippit_enabled_and_correct():
    os.environ['FEATURE_JEFF_IS_JEFF'] = '1'
    
    flipped_func = flipper.flippit('jeff_is_jeff',
                                   fake_new_func,
                                   fake_old_func)

    assert flipped_func() == 'new'

    flipped_func = flipper.flippit('jeff_is_jeff',
                                   fake_new_func)

    assert flipped_func() == 'new'

    flipped_func = flipper.flippit('jeff_is_jeff')

    assert flipped_func() == None

def test_flippit_enabled_and_incorrect():
    os.environ['FEATURE_JEFF_IS_JEFF'] = '1'
    
    flipped_func = flipper.flippit('jeff_is_jef',
                                   fake_new_func,
                                   fake_old_func)

    assert flipped_func() == 'old'

    flipped_func = flipper.flippit('jeff_is_jef',
                                   fake_new_func)

    assert flipped_func() == None

    flipped_func = flipper.flippit('jeff_is_jef')

    assert flipped_func() == None

    del os.environ['FEATURE_JEFF_IS_JEFF']

def test_flippit_disabled():
    os.environ['FEATURE_JEFF_IS_JEFF'] = '0'
    flipped_func = flipper.flippit('jeff_is_jeff',
                                   fake_new_func,
                                   fake_old_func)

    assert flipped_func() == 'old'

    flipped_func = flipper.flippit('jeff_is_jeff',
                                   fake_new_func)

    assert flipped_func() == None

    flipped_func = flipper.flippit('jeff_is_jeff')

    assert flipped_func() == None

    del os.environ['FEATURE_JEFF_IS_JEFF']

def test_flippit_does_not_exist():
    flipped_func = flipper.flippit('jeff_is_jeff',
                                   fake_new_func,
                                   fake_old_func)

    assert flipped_func() == 'old'

    flipped_func = flipper.flippit('jeff_is_jeff',
                                   fake_new_func)

    assert flipped_func() == None

    flipped_func = flipper.flippit('jeff_is_jeff')

    assert flipped_func() == None
