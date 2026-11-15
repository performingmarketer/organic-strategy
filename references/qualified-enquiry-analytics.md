# Organic Qualified Enquiry Scorecard and attribution

## Funnel definition before metric selection

**Discovery** (GSC impressions, social reach; measured in their own systems) → **meaningful attention** (GSC clicks, engaged sessions, video watch time/saves) → **intent** (service page views, profile contacts, voluntary enquiry) → **qualification** (matched service, correct region, sufficient interest) → **verified outcome** (booking completed, counselling attended, admission, sale). Events across tools are not automatically deduplicated.

Choose *one* business-specific north-star: e.g. **qualified WhatsApp enquiry**, **attended appointment**, **verified admission** or **purchase**. A generic “lead” is not a qualified lead.

## Practical scorecard

| KPI | Definition | Data source | Frequent interpretation error |
|---|---|---|---|
| Organic search clicks | GSC clicks in defined search filters/date range | GSC | Not identical to GA4 sessions or unique people |
| Organic landing-page actions | User-defined GA4 key events after an eligible visit | GA4 | Events require configuration and validation |
| GBP interactions | Reported calls, requests and interactions as available | GBP Performance | Not equivalent to visits or confirmed customers |
| Social meaningful actions | Link click, profile contact, opted-in DM, saves as defined | Native insights + CRM | Reach/saves are not admissions or sales |
| Qualified enquiry rate | Verified qualified enquiries ÷ all eligible tracked enquiries ×100 | CRM + lead intake | Need consistent definitions and deduplication |
| Lead-to-outcome rate | Verified outcomes ÷ eligible qualified leads ×100 | CRM | Do not mix cohorts or windows |
| Content effort per qualified lead | Logged cost/time of eligible production ÷ qualified leads | Content cost ledger + CRM | Not Meta Ads CPL; attribution may be partial |

**Zero-denominator handling:** use `N/A — no eligible observations`, never divide by zero or hide this as 0%.

## Minimal privacy-aware lead ledger

`lead_id (random non-identifying) | received_at | source_reported | tracked_utm_source/medium/campaign/content | source_confidence | service_interest | region_fit | qualification_status | follow_up_status | booked_attended | verified_outcome | evidence_date | owner`

Keep only necessary data, seek consent, access-control exports and avoid exposing real phone numbers in sample outputs. Qualification must come from the business's actual acceptance criteria, not guesses about demographics or sensitive traits.

## Attribution standards

- **Tracked:** a link with appropriate UTM tags or first-party events where implemented; can be incomplete.
- **Self-reported:** the customer says “saw your reel”; useful but not precise marketing attribution.
- **Assisted:** an observed touchpoint was involved; cannot infer its individual causal effect from ordinary analytics.
- **Unknown:** no defensible source; **do not assign this to organic social**.
- For multi-touch / duplicates, track unique leads separately from touch events.
- Do not present a Google Search Console increase as more customers, and do not claim Instagram content directly raises Google rankings.

## When given data

Require timeframe, filter/source, baseline, metric definition and sample size. Show calculations only for supplied data. Explain possible seasonality, tracking changes and demand shifts, especially for small data. Propose next evidence collection rather than declaring causation.

## 4-week review routine

Week 1 define funnel and validate links/events; Week 2 inspect content usefulness and enquiry flow; Week 3 review segment fit and proof gaps; Week 4 compare like-for-like KPI periods and choose **keep / improve / replace / investigate**. Search learning can be much slower; four weeks is a work cadence, not a ranking guarantee.