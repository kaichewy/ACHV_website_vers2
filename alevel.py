{% extends "base.html" %}
{% block content %}
<section>
    <div class="container-fluid no-padding ult-box1">
        <div class="row padding big-box">
            <div class="col-12 col-lg-6 padding right big-box2">
    <!--            <div class="image-wrapper box2">-->
    <!--                <img class="achv-logo" src="static/images/achv_logo_transparent.png" alt="ACHV" style="width: 500px; justify-content:center;">-->
    <!--            </div>-->
                <div id="carouselExampleSlidesOnly" class="carousel slide" data-ride="carousel" data-interval="2000">
                      <div class="carousel-inner">
                            <div class="carousel-item active big-box2">
                                <img class="achv-logo" src="static/images/achv_logo_transparent.png" alt="">
                            </div>
                            <div class="carousel-item big-box2">
                                <img class="achv-logo" src="static/images/achv_logo_transparent.png" alt="">
                            </div>
                      </div>
                </div>
            </div>
            <div class="col-12 col-lg-6 padding left big-box1">
                <h5 class="mbr-section-title mbr-fonts-style display-1 title"><span>CRASH</span> COURSES</h5>
                <h1 class="mbr-section-subtitle mbr-fonts-style display-7 ">Are what we specialise in and offer to help
                    Singaporean students achieve their academic goals.</h1>
                <div class="btn-div">
                  <button class="btn btn-dark btn-lg sign-up-button btn-in-btn-div" type="button"><i class="fa-solid fa-right-to-bracket"></i>   Sign Up Now</button>
                  <button class="btn btn-light btn-lg learn-more-button btn-in-btn-div" type="button"><i class="fa-solid fa-school"></i>   Learn More</button>
                </div>
            </div>
        </div>
    </div>
</section>

<section>
<div class="container">
    <div class="row features">
      <div class="col-sm-12 col-md-4">
        <div class="Two Options">
          <i class="fa-solid fa-star fa-bounce fa-4x" style="color: #fffb8a;"></i>
          <div class="caption">
            <h3>Special Attention</h3>
            <p>We offer two types of classes, one class for stronger students who aspire to
            secure the good grade they've always achieved in their internal exams, and another class
            for weaker students who have always struggled.
            </p>
          </div>
        </div>
      </div>
  <div class="col-sm-12 col-md-4">
    <div class="thumbnail">
      <div class="caption">
            <i class="fa-solid fa-user-tie fa-beat fa-4x" style="color: #000000;"></i>
        <h3>IDK WHAT TO SAY</h3>
        <p>We offer two types of classes, one class for stronger students who aspire to secure the good grade they've always achieved in their internal exams, and another class for weaker students who have always struggled.</p>
      </div>
    </div>
  </div>
  <div class="col-sm-12 col-md-4">
    <div class="thumbnail">
        <i class="fa-solid fa-desktop fa-shake fa-4x" style="color: #fdbafb;"></i>
    <div class="caption">
        <h3>ONLINE</h3>
        <p>We offer two types of classes, one class for stronger students who aspire to secure the good grade they've always achieved in their internal exams, and another class for weaker students who have always struggled.</p>
      </div>
    </div>
  </div>
    </div>
</div>
</section>


<section class="moto-section">
    <div class="container moto-container">
        <div class="row justify-content-center">
            <div class="col-12">
                <div class="moto">
                    <h5 class="moto-line1">WE BELIEVE</h5>
                    <h2 class="moto-line2">EVERY STUDENT CAN</h2>
                    <div class="moto-line3">
                        <span class="brand-part">ACH</span><span class="not-brand-part">IE</span><span class="brand-part">V</span><span class="not-brand-part">E</span>
                    </div>
<!--                    <div>-->
<!--                        <img class="achv-logo2" src="static/images/achv_logo_transparent.png" alt="">-->
<!--                    </div>-->
                </div>
            </div>
        </div>
    </div>
</section>

<section>
    <div class="more-about-us">
        <h1 class="more-about-us-title">MORE ABOUT US</h1>
    </div>
</section>

<section id="pricing">

    <h2>A Plan for Every Student's Needs</h2>
    <p>.</p>


    <div class="card-deck text-center">
      <div class="card">
        <div class="card-body">
          <h3 class="card-title">NO TIME TO WASTE</h3>
          <h2 class="card-title">Free</h2>
          <p class="card-text">5 Matches Per Day</p>
          <p class="card-text">10 Messages Per Day</p>
          <p class="card-text">Unlimited App Usage</p>
          <a href="#" class="btn btn-primary">Sign Up</a>

        </div>

      </div>
      <div class="card">
        <div class="card-body">
          <h3 class="card-title">IDK WHAT TO WRITE</h3>
          <h2 class="card-title">$49 / mo</h2>
          <p class="card-text">Unlimited Matches</p>
          <p class="card-text">Unlimited Messages</p>
          <p class="card-text">Unlimited App Usage</p>
          <a href="#" class="btn btn-primary">Sign Up</a>

        </div>

      </div>
      <div class="card">
        <div class="card-body">
          <h3 class="card-title">GRANDE</h3>
          <h2 class="card-title">$99 / mo</h2>
          <p class="card-text">Priority Listing</p>
          <p class="card-text">Unlimited Matches</p>
          <p class="card-text">Unlimited Messages</p>
          <p class="card-text">Unlimited App Usage</p>
          <a href="#" class="btn btn-primary">Sign Up</a>
        </div>

      </div>
    </div>

</section>


  <!-- Call to Action -->

<section id="cta">
    <h3>Choose Us And Achieve Only The Best.</h3>
    <button class="btn btn-light btn-lg sign-up-button btn-in-btn-div" type="button"><i class="fa-solid fa-right-to-bracket"></i>   Sign Up Now</button>
</section>

<footer id="footer">
    <i class="fa-brands fa-twitter footer-icon"></i>
    <i class="fa-brands fa-facebook footer-icon"></i>
    <i class="fa-brands fa-instagram footer-icon"></i>
    <i class="fa-solid fa-envelope footer-icon"></i>
    <p>© Copyright 2023 ACHV</p>
</footer>

{% endblock %}
