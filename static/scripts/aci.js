// An ACI fabric
var AciFabric = React.createClass({displayName: 'AciFabric',
  getInitialState: function() {
    return {data: []};
  },

  loadTenantsFromServer: function() {
  $.ajax({
    url: this.props.url,
    dataType: 'json',
    cache: false,
    success: function(data) {
      this.setState({data: data});
    }.bind(this),
    error: function(xhr, status, err) {
      console.error(this.props.url, status, err.toString());
    }.bind(this)
  });
},
  componentDidMount: function() {
    this.loadTenantsFromServer();
    setInterval(this.loadTenantsFromServer, this.props.pollInterval);
},
  render: function() {
    return (
      <div className="aciFabric">
        <TenantList data={this.state.data} />
      </div>
      )
  }
});

// A tenant list
 var TenantList = React.createClass({
   render: function() {
      var tenantNodes = this.props.data.map(function(tenant) {
        return (
          <AciTenant name={tenant.name}
            score={tenant.score}
            descr={tenant.descr}
            crit={tenant.crit}
            maj={tenant.maj}
            warn={tenant.warn}
            minor={tenant.minor}
            key={tenant.dn}>
            {tenant.descr}
          </AciTenant>
        );
      });
      return (
        <div className="tenantList">
          {tenantNodes}
        </div>
      );
    }
  });


 var AciTenant = React.createClass({

   render: function() {
     return (
       // This is where we render the html representation of the object
       // <div className="foo"> here will render as <div class="foo">
       // start as a simple list, comment this line out and add your code below

       <li>{this.props.name} - {this.props.score}</li>

     // End html representation
   );
   }

 });
