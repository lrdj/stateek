---
layout: unbranded
title: Stateek index page
---

1. one
2. two
3. three

- list
- list
- list

# H1 header

## X Posts

<div class="govuk-grid-row">
    <div class="govuk-grid-column-two-thirds">
    	
		<h1 class="govuk-heading-xl" style="font-size:3rem;">{{ page.title }}</h1>
		<p class="govuk-body-l">Text on index page</p>

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a> – <small>{{ post.date | date: "%B %-d, %Y" }}</small>
    </li>
  {% endfor %}
</ul>


    
    </div>
</div>

