# ACM Research Coding Challenge S23

## Short and Sweet Summary

<img src="https://sugargeekshow.com/wp-content/uploads/2022/08/vanilla_cupcakes_featured-scaled.jpg" alt="A sweet and short cupcake, like this summary" width="250" height="250">

*I made a partial HR Diagram that can be clicked to show closest star to click location.*

## The Long Road Home Report

<img src="https://www.msbaptistfoundation.org/hp_wordpress/wp-content/uploads/2020/09/road-1024x682.jpg" alt="Did you ever hear the tragedy of darth plagueis the wise... yadda yadda you get the point" width="250" height="250">

### Goals
I started out by browsing the data set for interesting information and just seeing if anything popped out. I had used HR Diagrams in middle school science before, so I planned to replicate one of those to start with and see where this visualization took me.

### Research
I started familiarizing myself with what exactly an HR Diagram was and what it was used for. Essentially, they can be used to track the life cycle of stars and model different stages like *Supergiants* and *White Dwarfs*. Their axes are either temperature in kelvin v. luminosity in solar luminosity or spectral class v. absolute visual magnitude depending on whether the HR Diagram is the theoretical or observational version with some diagrams featuring both. Additionally, the temperature axis inverted from hottest to coldest and the luminosity axis is in a log scale.

### Coding
I wanted to learn more about the matplotlib package in python, specifically pyplot, so I began working on making a graph that would replicate an HR Diagram. I needed to reference the pyplot documentation quite a bit to learn the functions I could use to customize the graph such and the `ax.set_yscale("log")` and `ax.invert_xaxis()` functions that would make the HR Diagram appear. I initially tried to do a complete HR Diagram with both the theoretical and observational comparisons but I couldn't come up with an easy solution in a reasonable time for this *short* challenge, so I made do with only the theoretical axes[^1].

### More Coding
After completing the HR diagram, I knew I wanted to do some type of user input to affect the graph. I looked into the matplotlib animation and event handling documentation sections and explored. I came up with the idea to get the closest star to where the user clicked and began to implement that. I did this by getting the user's data position that was clicked on the plot and finding the actual point with the minimum distance to that position [^2]. I ended up needing to remove the observational HR diagram from the pair and only implement the closest point functionality on the theoretical HR[^3]. I then added a new line on the same HR plot that would connect the user's clicked position and the closest star[^4].

### Results

Here is the HR Diagram that generates on starting the python file:

<img src="/img/hr_imgreg.png" alt="Base HR Diagram generated" width="400" height="400">

Here is examples of the closest star functionality and the corresponding console output

<img src="/img/hr_imgline1.png" alt="Base HR Diagram generated" width="250" height="250">
<img src="/img/hr_imgline2.png" alt="Base HR Diagram generated" width="250" height="250">
<img src="/img/hr_imgline3.png" alt="Base HR Diagram generated" width="250" height="250">
<img src="/img/hr_imgtext.png" alt="Base HR Diagram generated" width="750" height="150">

The closest star functionality is accurate to the actual temperature and luminosity values but appears faulty from the third graph image with a line. This is due to how the y-axis of luminosity is log scaled and so graphical data is distorted and may confuse the user who is used to regularly scaled graphs.

### Future
If I had more time, I would devote time to creating a more accurate HR Diagram with both sets of axes as well as displaying the closest star's spectral class. Additionally, doing more serious data transformations would be interesting such as utilizing a clustering analysis algorithm to predict spectral classes and testing its accuracy the actual classes[^5].

### Bonus
The closest star in the data set to our sun is the star with these qualities `5587 0.819 0.99 5.03 3 yellow-white F`. This is due to the similar temperature between them *5587 v. 5400*, the similar luminosity *0.819 v. 1*, similar radius *0.99 v. 1*, similar absolute visual magnitude *5.03 v. 4.83*, similar color *yellow-white v. yellow*, and similar spectral class *F v. G*. This was just found in the course of research and was not found by any programs.

[^1]: I did make two adjacent plots work though, with theoretical HR on the left and observational HR on the right, but I would scrap the idea later in order to simplify my added functionality.
[^2]: I just did *(change in x)<sup>2</sup> + (change in y)<sup>2</sup>* to compute distance instead of adding the square root too because it doesn't change the result and square root is an expensive calculation in optimization if that mattered at all.
[^3]: Fixing this and creating a complete HR diagram would just take more time I didn't need to use
[^4]: I just realized I forgot to output the closest star's spectral type as I originally planned. This would be implemented by intially mapping each temperature-position (x-y) pair to a their respective spectral class in a dictionary and saving that to key in and print later when the closest point was computed. 
[^5]: I really like this idea now actually.

