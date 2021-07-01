<h1 align="center">Pre-filter RR intervals for Heart Rate Variability analysis</h1>

<h3 align="justify">Pre-filtering .txt files exported from <a href="https://support.polar.com/en/support/V800">PolarV800</a>, <a href="https://www.polar.com/us-en/products/accessories/h10_heart_rate_sensor">Polar H10</a> and/or <a href="https://elitehrv.com/">EliteHRV</a> devices with RR intervals for heart rate variability analysis.</h3>

<p align="justify"><a href="https://en.wikipedia.org/wiki/Heart_rate_variability">Heart rate variability</a> (HRV) :heart: is a powerful and inexpensive health indicator. Is the physiological phenomenon of variation in the time interval between heartbeats. It is measured by the variation in the beat-to-beat interval. In the RR interval, R is a point corresponding to the peak of the QRS complex of the electrocardiogram wave; and RR is the interval between successive Rs.</p>
<p align="justify">Nowadays, many devices capture RR intervals for HRV analysis, among them is PolarV800, PolarH10 sensor belt and EliteHRV App. Both generate a txt file with the record of the intervals that will later be analyzed in the appropriate software.</p>
<h3>This code reads the txt files from a directory, pre-filters the intervals and generates other txt files that can be used in the analysis.</h3>
<p>For each file:</p>
<ul>
  <li>Remove the minimum values until they are repeated</li>
	<li>Removes the maximum values until they are repeated</li>
	<li>If necessary (for the Polar device), convert the values to milliseconds and exclude the accumulated time</li>
	<li>Creates a pre-filtered txt file with RR intervals</li>
  <li>Creates a file with the first 256 pre-filtered RR intervals, if there are enough intervals</li>
  <li>Creates a file with the first 1000 pre-filtered RR intervals, if there are enough intervals</li>
</ul>

<h3 align="center">:grey_exclamation: You may use the samples in diretory <a href="https://github.com/edudati/filteringHRV/tree/main/files">"files"</a> and see how it works. :grey_exclamation:</h3>
