<h1 align="center">Pre-filter RR intervals</h1>

<h3 align="justify">pre-filtering .txt files exported from PolarV800 and EliteHRV devices with RR intervals for heart rate variability analysis.</h3>

<p align="justify"><a href="https://en.wikipedia.org/wiki/Heart_rate_variability">Heart rate variability (HRV)</a> is the physiological phenomenon of variation in the time interval between heartbeats. It is measured by the variation in the beat-to-beat interval. Other terms used include: "cycle length variability", "RR variability" (where R is a point corresponding to the peak of the QRS complex of the ECG wave; and RR is the interval between successive Rs), and "heart period variability".</p>
<p align="justify">Nowadays, many devices capture RR intervals for HRV analysis, among them is PolarV800 and EliteHRV App. Both generate a txt file with the record of the intervals that will later be analyzed in the appropriate software.</p>
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

<p>You may use the samples in diretory "files" and see how it works</p>




