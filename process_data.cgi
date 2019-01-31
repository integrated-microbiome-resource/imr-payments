#!/usr/bin/perl -w

use strict;
use warnings;
#use Digest::HMAC_SHA1 qw(hmac_sha1_hex);
use Digest::SHA qw(sha1_hex);
use FormValidator::Simple;
use CGI qw(:standard);

#  Validate submitted form data
my $query = CGI->new;
	$query->param('cust_id');
	$query->param('invoice_num');
	$query->param('amount');

my $result = FormValidator::Simple->check( $query => [
        ordName => ['NOT_BLANK', ['LENGTH', 1, 70]],
	ordEmailAddress => ['NOT_BLANK', ['LENGTH', 1, 70]],
        invoice_num => ['NOT_BLANK', ['LENGTH', 1, 4]],
        amount  => ['NOT_BLANK', ['DECIMAL', 5, 2], ['LENGTH', 2, 8]],
    ] );

# if any errors in form data, print error page
if ( $result->has_error )
{

print <<END;
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
<head>
<title>IMR Payment Error</title>
<script src="js/jquery.min.js"></script>
                <script src="js/jquery.dropotron.min.js"></script>
                <script src="js/jquery.scrolly.min.js"></script>
                <script src="js/jquery.onvisible.min.js"></script>
                <script src="js/skel.min.js"></script>
                <script src="js/skel-layers.min.js"></script>
                <script src="js/init.js"></script>
                <noscript>
                        <link rel="stylesheet" href="css/skel.css" />
                        <link rel="stylesheet" href="css/style.css" />
                        <link rel="stylesheet" href="css/style-desktop.css" />
                        <link rel="stylesheet" href="css/style-noscript.css" />
                </noscript>
                <!--[if lte IE 8]><link rel="stylesheet" href="css/ie/v8.css" /><![endif]-->
        </head>
        <body class="no-sidebar">
                        <div id="header">
                                        <div class="inner">
                                                <header>
                                                        <h1><a href="http://cgeb-imr.ca/" id="logo">Integrated Microbiome Resource (IMR)</a></h1>
                                                </header>
                                        </div>
                                        <nav id="nav">
                                                <ul>
                                                        <li><a href="http://cgeb-imr.ca/index.html">Home</a></li>
                                                        <li><a href="http://cgeb-imr.ca/about.html">About Us</a></li>
                                                        <li><a href="http://cgeb-imr.ca/achieve.html">Achievements</a></li>
                                                        <li><a href="http://cgeb-imr.ca/submissions.html">Submission Guidelines</a></li>
                                                        <li><a href="http://cgeb-imr.ca/queue.html">Real-Time Queue</a></li>
                                                        <li><a href="http://cgeb-imr.ca/pricing.html">Pricing</a></li>
                                                        <li><a href="http://cgeb-imr.ca/protocols.html">Protocols</a></li>
                                                        <li><a href="http://cgeb-imr.ca/contact.html">Contact Us</a></li>
                                                </ul>
                                        </nav>

                        </div>
                        <div class="wrapper style1">
                                <div class="container">
                                        <article id="main" class="special">
                                                <header>
                                                        <h2>Payment Details Error</h2>
                                                </header>
                                                <section>
                                                        <p><font color="red">Your submitted information has generated an error! Please verify the below requirements, then return to the <a href="http://payment.cgeb-imr.ca">Payment Info Page</a> to retry.
                                                        <p><b>Client Name: <font color="red">Must only be ASCII characters and not blank!</font></b>
							<p><b>Client Email: <font color="red">Must only be ASCII characters and not blank!</font></b>
                                                        <p><b>Invoice Number: <font color="red">Numbers plus (optionally) one letter only, no spaces - up to four (4) characters are allowed!</font></b>
                                                        <p><b>Amount: <font color="red">Numbers only, no spaces - up to eight (8) characters are allowed, including the period (ie: 12345.67)!</font></b>
                                                        </p>
                                                </section>
                                        </article>
                                        </div>
                                </div>

                        </div>
                        <div id="footer">
                                                                <div class="copyright">
                                                                        <ul class="menu">
                                                                                <li>&copy; CGEB-IMR (2014+). All rights reserved.</li><li>Design template: <a href="http://html5up.net" target="new">HTML5 UP</a></li>
                                                                        </ul>
                                                                </div>

                        </div>
        </body>
END

}
else
{
# no errors, continue script using the input

#  Define submitted form data 
my $ordName = param('ordName');
my $ordEmailAddress = param('ordEmailAddress');
my $trnOrderNumber = param('invoice_num');
my $trnAmount = param('amount');

#  Required extra parameters
my $merchant_id = "117687525";  
my $hash_key = ""; # Take from configuration interface
#my $x_currency_code = "CAD"; # Needs to agree with the currency of the payment page
#my $x_fp_sequence = int(rand 5000) + 1000;
#my $x_fp_timestamp = time; #  needs to be in UTC. Make sure webserver produces UTC

#  The values that contribute to sha1 hash
# Note: the hash key is simply appended to the end of the string before being hashed
my $hmac_data = "merchant_id=".$merchant_id . "&" ."trnAmount=". $trnAmount . "&" ."trnOrderNumber=". $trnOrderNumber . $hash_key;

#  Calculate the value of the x_fp_hash
my $hashValue = sha1_hex($hmac_data);

print <<END;
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
<head>
<title>CGEB-IMR Payment Confirmation</title>
<script src="js/jquery.min.js"></script>
		<script src="js/jquery.dropotron.min.js"></script>
		<script src="js/jquery.scrolly.min.js"></script>
		<script src="js/jquery.onvisible.min.js"></script>
		<script src="js/skel.min.js"></script>
		<script src="js/skel-layers.min.js"></script>
		<script src="js/init.js"></script>
		<noscript>
			<link rel="stylesheet" href="css/skel.css" />
			<link rel="stylesheet" href="css/style.css" />
			<link rel="stylesheet" href="css/style-desktop.css" />
			<link rel="stylesheet" href="css/style-noscript.css" />
		</noscript>
		<!--[if lte IE 8]><link rel="stylesheet" href="css/ie/v8.css" /><![endif]-->
	</head>
	<body class="no-sidebar">
			<div id="header">
					<div class="inner">
						<header>
							<h1><a href="http://cgeb-imr.ca/" id="logo">Integrated Microbiome Resource (IMR)</a></h1>
						</header>
					</div>
					<nav id="nav">
						<ul>
							<li><a href="http://cgeb-imr.ca/index.html">Home</a></li>
							<li><a href="http://cgeb-imr.ca/about.html">About Us</a></li>
							<li><a href="http://cgeb-imr.ca/achieve.html">Achievements</a></li>
							<li><a href="http://cgeb-imr.ca/submissions.html">Submission Guidelines</a></li>
							<li><a href="http://cgeb-imr.ca/queue.html">Real-Time Queue</a></li>
							<li><a href="http://cgeb-imr.ca/pricing.html">Pricing</a></li>
							<li><a href="http://cgeb-imr.ca/protocols.html">Protocols</a></li>
							<li><a href="http://cgeb-imr.ca/contact.html">Contact Us</a></li>
						</ul>
					</nav>

			</div>
			<div class="wrapper style1">
				<div class="container">
					<article id="main" class="special">
						<header>
							<h2>Confirm Payment Details</h2>
						</header>
						<section>
							<p>Please confirm your submitted information below and click <b>Proceed to Checkout</b> - you will then be taken to our secure payment site. If you need to change the submitted values, return to the <a href="http://payment.cgeb-imr.ca/">Payment Input</a> page.
							<p><b>Client Name: $ordName</b>
							<p><b>Email: $ordEmailAddress</b>
							<br><br><b>Invoice #: $trnOrderNumber</b>
							<br><br><b>Amount to pay: $trnAmount CAD</b>
							<form action="https://web.na.bambora.com/scripts/payment/payment.asp" method="post">
							  <input name="merchant_id" value="$merchant_id" type="hidden">
							  <input name="trnAmount" value="$trnAmount" type="hidden">
							  <input name="trnOrderNumber" value="$trnOrderNumber" type="hidden">
							  <input name="hashValue" value="$hashValue" type="hidden">
							  <input name="ordEmailAddress" value="$ordEmailAddress" type="hidden">
							  <input name="ordName" value="$ordName" type="hidden">							  
							  <input name="x_show_form" value="PAYMENT_FORM" type="hidden">
							  <input value="Proceed to Checkout" type="submit">
							</form>
							</p>
						</section>
					</article>
					</div>
				</div>

			</div>
			<div id="footer">
								<div class="copyright">
									<ul class="menu">
										<li>&copy; CGEB-IMR (2014+). All rights reserved.</li><li>Design template: <a href="http://html5up.net" target="new">HTML5 UP</a></li>
									</ul>
								</div>
							
			</div>
	</body>
END
}
