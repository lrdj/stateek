---
layout: unbranded
title: "Getting Started with Jekyll"
date: 2025-06-01 12:00:00 -0500
categories: jekyll tutorial
comments:
  - email: john.doe@example.com
    nickname: JohnD
    date: 2025-06-01T14:30:00Z
    message: "This is a fantastic introduction to Jekyll! I've been looking for something like this for a while."
  - email: jane.smith@example.com
    nickname: JaneS
    date: 2025-06-01T15:45:00Z
    message: "Thanks for the clear explanation. I was wondering if you could elaborate more on collections in a future post?"
  - email: anonymous@example.com
    nickname: 
    date: 2025-06-01T18:20:00Z
    message: "I'm new to static site generators. Is Jekyll suitable for a blog with around 100 posts?"
---


<div class="govuk-grid-row">
    <div class="govuk-grid-column-two-thirds">
    	
		<h1 class="govuk-heading-xl">{{ page.title }}</h1>
		<p class="govuk-body-l">
		Jekyll is a powerful tool for creating static websites with minimal effort. Its simplicity and flexibility make it an excellent choice for blogs, documentation sites, and more.</p>

		<h2 class="govuk-heading-l">Conclusion</h2>

    </div>
</div>

{% include comment-form.html %}

