After running the tests, we see that the first thing to fail is that 
the `Chair` object does not have the attribute `capacity` so, let's go and add only that 
to our class. 
 
 . . . . . . . 
 
After adding that we see that the `Exception` we were expecting was not raised. 
Fix only that and import the exception in our tests (we should have done this previously)

 . . . . . . . 

Now the error is different, `Chair` is missing a method, let's fix it and do 
nothing inside it.

 . . . . . . . 
 
Up's, it needs to take mor arguments than just `self`, add a parameter called, `capacity` 
and run the tests again

 . . . . . . . 

Because the chair is blue, it can only take one person, raise our exception if that is 
the case, rerun the tests 

 . . . . . . . . 
 
`None is not true` ! The tests even tell you what your function should return

. . . . . . .  